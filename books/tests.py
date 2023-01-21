from django.test import TestCase
from django.urls import reverse
from .models import Book


# har bir test yozganda malumotlar bazasi avtomatik yangilanadi va bosh xolatga keladi
class BookTestCase(TestCase):

    # 1. test book listni ichida product bormi yoqmi deb tekshirish
        def test_no_books(self):
            response = self.client.get(reverse('books:list'))
            # 1. Book listni ichida hechnarsa yoq degan error chiqadimi yoqmi tekshirib olamiz
            # bu ikkta method qabul qiladi
            self.assertContains(response, 'No books found.')


    # 2. test booklarni title bormi degan


        def test_books_list(self):
          book1 = Book.objects.create(title='Books1', description='nimadur gapla', isbn='1234356464', )
          book2 = Book.objects.create(title='Books2', description='nimadur gapld', isbn='12343564644', )
          book3 = Book.objects.create(title='Books3', description='nimadur gaplare', isbn='12343564645', )
        # pagination test 1 chi 2 pagega response junatdim
          response = self.client.get(reverse('books:list'))

          for book in [book1,book2]:
               self.assertContains(response, book.title)

        #  va ikkinchi testga response yubordim
          response = self.client.get(reverse('books:list') + '?page=2' )
        # 3. title ni bosganda boshqa pagega olib otadimi degan test

        def test_detail_page(self):
            book = Book.objects.create(
                title='Books1', description='nimadur gapla', isbn='1234356464', )
            response = self.client.get(
                reverse('books:detail', kwargs={'id': book.id}))
            self.assertContains(response, book.title)
            self.assertContains(response, book.description)

        def test_search_books(self):
            book1 = Book.objects.create(title='Sport', description='nimadur gapla', isbn='1234356464', )
            book2 = Book.objects.create(title='Abror', description='nimadur gapld', isbn='12343564644', )
            book3 = Book.objects.create(title='Hostel', description='nimadur gaplare', isbn='12343564645', )

            response = self.client.get(reverse('books:list') + '?q=Sport')
            self.assertContains(response, book1.title)
            self.assertNotContains(response, book2.title)
            self.assertNotContains(response, book3.title)

            # response = self.client.get(reverse('books:list') + '?q=Abror')
            # self.assertContains(response, book2.title)
            # self.assertNotContains(response, book1.title)
            # self.assertNotContains(response, book3.title)
            #
            # response = self.client.get(reverse('books:list') + '?q=Hostel')
            # self.assertContains(response, book3.title)
            # self.assertNotContains(response, book1.title)
            # self.assertNotContains(response, book2.title)
