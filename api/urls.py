from django.urls import path
# from .views import BookReviewDetailApiView,BookListAPIView
from rest_framework.routers import DefaultRouter
from api.views import BookReviewsViewSet

app_name = 'api'
router = DefaultRouter()
router.register(r'reviews', BookReviewsViewSet, basename='review')
urlpatterns = router.urls
# qolda yozilgan viewlarni pathlari
# path('reviews/',  BookListAPIView.as_view(), name='review-list'),
# path('reviews/<int:id>/', BookReviewDetailApiView.as_view(), name='review-detail')
