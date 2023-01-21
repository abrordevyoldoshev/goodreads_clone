from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from books.models import Book, BookReview
from users.models import CustomUser


class BookReviewApiTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="jakhongir", first_name="Jakhongir")
        self.user.set_password("somepass")
        self.user.save()
        self.client.login(username="jakhongir", password="somepass")

    def test_book_review_detail(self):
        book = Book.objects.create(title='Books11', description='nimadur gaplas', isbn='12343564643', )
        br = BookReview.objects.create(book=book, user=self.users, starts_given=5, commit='Very goot book')
        response = self.client.get(reverse('api:review-detail', kwargs={'id': br.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], br.id)
        self.assertEqual(response.data['starts_given'], 5)
        self.assertEqual(response.data['commit'], 'Very goot book')

