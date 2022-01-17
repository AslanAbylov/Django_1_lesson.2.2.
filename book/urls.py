from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books, name='books'),
    path('books/<int:id>/', views.books_detail, name='books_detail'),
    path('add-book/', views.add_book, name='add_book'),

]
