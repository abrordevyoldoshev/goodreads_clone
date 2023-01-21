from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets

from books.models import BookReview
from .serializers import BookReviewSerializers


# qisqa yozilgan udate create delet get codlar
class BookReviewsViewSet(viewsets.ModelViewSet):
    # 0. login qilingan userlarni tekshiradi
    permission_classes = [IsAuthenticated]
    # 1. qaysi serializer_class da ishlay degan savolga BookReviewSerializers ishla
    serializer_class = BookReviewSerializers
    # 2. qaysi queryset ustida ishlay deganda BookReview hammasini ustida ishla
    queryset = BookReview.objects.all().order_by('-created_at')
    # 3. qaysi field orqali malumotlarni topay degan savolga (id) deb beramiz
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        # agar ozgartirish kiritmoqchi bolsam shu bilan ozgartirib ketaman
        pass

# qolda yozilgan udate create delet get codlar
# -----------------------------------------------------------------------------
# class BookReviewDetailApiView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     # 1. qaysi serializer_class da ishlay degan savolga BookReviewSerializers ishla
#     serializer_class = BookReviewSerializers
#     # 2. qaysi queryset ustida ishlay deganda BookReview hammasini ustida ishla
#     queryset = BookReview.objects.all()
#     # 3. qaysi field orqali malumotlarni topay degan savolga (id) deb beramiz
#     lookup_field = "id"
#
#
# class BookListAPIView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BookReviewSerializers
#     queryset = BookReview.objects.all().order_by('-created_at')

# -------------------------------------------------------------------------------------------
# from rest_framework.views import APIView dan meros oladi
# 1. bular qolda yozilgan update delete codlari
# -----------------------------------------------------------------
# def get(self, request, id):
#     book_review = BookReview.objects.get(id=id)
#     serializers = BookReviewSerializers(book_review)
#     return Response(data=serializers.data)
#
# def delete(self, request, id):
#     book_review = BookReview.objects.get(id=id)
#     book_review.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
#
# #
# # def put(self, request, id):
# #     book_review = BookReview.objects.get(id=id)
# #     serializers = BookReviewSerializers(instance=book_review, data=request.data)
# #
# #     if serializers.is_valid():
# #         serializers.save()
# #         return Response(data=serializers.data, status=status.HTTP_200_OK)
# #     else:
# #
# #         return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
# # <--------------------------------------------------------------------------------------------->
# # patch bilan put ni farqi put da update qilmoqchi bolsa hamma malimotni ozgartirish ketak bolmasa xato beradi
# # patch da esa istagan malumotni ozgartiskaham qolganlarini ham ozgartirish shar demaydi ishlayveradi
#
# def patch(self, request, id):
#     book_review = BookReview.objects.get(id=id)
#     serializers = BookReviewSerializers(instance=book_review, data=request.data)
#
#     if serializers.is_valid():
#         serializers.save()
#         return Response(data=serializers.data, status=status.HTTP_200_OK)
#     else:
#
#         return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# 2. bular qolda yozilgan created qilish va get oll qilish codi
# -----------------------------------------------------------------
# APIView
# get all BookReview
# def get(self, request):
#     # book review larni hammasini olish
#     book_review = BookReview.objects.all().order_by('-created_at')
#     paginator = PageNumberPagination()
#     page_obj = paginator.paginate_queryset(book_review,request)
#     serializers = BookReviewSerializers(page_obj, many=True)
#     return paginator.get_paginated_response(serializers.data)
#
# def post(self, request):
#     serializers = BookReviewSerializers(data=request.data)
#     if serializers.is_valid():
#         serializers.save()
#         return Response(data=serializers.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
