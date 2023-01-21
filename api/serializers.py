
from rest_framework import serializers

from books.models import Book, BookReview
from users.models import CustomUser


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'isbn')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class BookReviewSerializers(serializers.ModelSerializer):
    # ( read_only = True ) faqat malumotni get qilganda ishlat degani update qilganda esa ishlamaydi masalan coment
    # va boshqa malumotlar uchsaham user bilan book ochamaydi
    user = UserSerializers(read_only=True)
    book = BookSerializers(read_only=True)
    # bu ikkalasi post qilganda kerak boladi aniq post qilish uchun
    # ( write_only = True ) malumotli create qilgan paytimizda id ber degani get qildanimizda ishlamaydi
    book_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BookReview
        fields = ('id', 'starts_given', 'commit', 'book', 'user', 'book_id', 'user_id')
