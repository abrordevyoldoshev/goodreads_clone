from django import forms

from books.models import BookReview


class BookReviewForm(forms.ModelForm):
    starts_given = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = BookReview
        fields = ('starts_given', 'commit')
