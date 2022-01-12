from django.urls import path
from book import views

urlpatterns = [
    path('books/', views.get_books, name='books'),
]
