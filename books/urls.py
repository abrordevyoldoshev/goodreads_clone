from django.urls import path
from .views import BooksView, BookDetailView, AddReviewForm, EditReview,ConfirmDeleteReviewView,DeleteReviewView

app_name = 'books'
urlpatterns = [
    path('', BooksView.as_view(), name='list'),
    path('<int:id>/', BookDetailView.as_view(), name='detail'),
    path('<int:id>/reviews/', AddReviewForm.as_view(), name='reviews'),
    path('<int:book_id>/reviews/<int:review_id>/edit>', EditReview.as_view(), name='edit_review'),
    path('<int:book_id>/reviews/<int:review_id>/delete/confirm>',
         ConfirmDeleteReviewView.as_view(), name='confirm-delete-review'),
    path('<int:book_id>/reviews/<int:review_id>/delete/>',
         DeleteReviewView.as_view(), name='delete-review')
]
