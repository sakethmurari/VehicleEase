from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_vehicle, name='book_vehicle'),
]
