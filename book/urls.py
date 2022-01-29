from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('books/', views.get_books, name='books'),
    path('books/<int:id>/', views.books_detail, name='books_detail'),
    path('books/<int:id>/update/', views.book_update, name='book_update'),
    path('books/<int:id>/delete/', views.book_delete, name='book_delete'),
    path('add-book/', views.add_book, name='add_book'),

]