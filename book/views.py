from django.shortcuts import render
from django.shortcuts import render
from book.models import Book
from book import models


def get_books(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})
