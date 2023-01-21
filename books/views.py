from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import BookReviewForm
from .models import Book
from .models import BookReview
from django.views.generic import ListView


# Create your views here.
# generic get qilish uchun ishlatiladi
# class BooksView(ListView):
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()
#     context_object_name = "books"
# paginate_by = 2


class BooksView(LoginRequiredMixin, View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q', '')
        if search_query:
            books = books.filter(title__icontains=search_query)
        page_size = request.GET.get('page_size', 2)
        paginator = Paginator(books, page_size)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        return render(request, 'books/list.html', {'page_obj': page_obj, 'search_query': search_query})


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm()
        return render(request, 'books/detail.html', {'book': book, 'review_form': review_form})


class AddReviewForm(LoginRequiredMixin, View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            # review create qilish
            BookReview.objects.create(
                # book  book = Book.object.get(id=id) dan kelgan book
                book=book,
                # user esa requestdan kelgan user login qilingan userlarni tekshirish uchun {LoginRequiredMixin}
                user=request.user,
                #  bu ikalasi form dan kelagan
                starts_given=review_form.cleaned_data['starts_given'],
                commit=review_form.cleaned_data['commit']
            )
            return redirect(reverse('books:detail', kwargs={'id': book.id}))

        return render(request, 'books/detail.html', {'book': book, 'review_form': review_form})


class EditReview(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        # book bilan review ni get qilib olngan bu 2 ta codeda
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        # editeda isinstance beriladi chunki qaysi review edite qilishmizni bildirish uchun
        review_form = BookReviewForm(instance=review)
        return render(request, 'books/edit_review.html', {'book': book, 'review': review, 'review_form': review_form})

    def post(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review, data=request.POST)

        if review_form.is_valid():
            review_form.save()
            return redirect(reverse('books:detail', kwargs={'id': book.id}))
        else:
            return render(request, 'books/edit_review.html', {'book': book, 'review': review, 'review_form': review_form})


class ConfirmDeleteReviewView(LoginRequiredMixin, View):

    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        return render(request, 'books/confirm_delete_review.html', {'book': book, 'review': review})


class DeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review.delete()
        messages.success(request, 'You have successfully delete this review')
        return redirect(reverse('books:detail', kwargs={'id': book.id}))
