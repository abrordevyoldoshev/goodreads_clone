from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from books.models import BookReview


def landing_page(request):
    # frontdan kelgan malumotlarni views lar bilan tutub gladioli
    # frontdan shunday yozuvli malumot keldi va buni HttpResponse() bilan tutub olindi
    # va buni urls ga ulab qoyildi

    return render(request, 'landing_page.html')


def home_page(request):  # -created_at dagi - eng yangi comment ni sort qilib chiqarib beradi
    book_review = BookReview.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size', 10)
    paginator = Paginator(book_review, page_size)
    page_number = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_objects': page_objects})
