from django.urls import path
from . import views


urlpatterns = [
    path('shows/', views.show_all, name='shows_all'),
    path('shows/<int:id>/', views.shows_detail, name='shows_detail'),
]