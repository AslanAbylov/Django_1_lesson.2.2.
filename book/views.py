from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from book.models import Book
from book import models


def get_books(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})

def books_detail(request, id):
    books = get_object_or_404(models.Book, id=id)
    return render(request, 'books_detail.html', {'books': books})