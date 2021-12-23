from django.urls import path, include
from . import views

app_name = 'category'

urlpatterns = [
    path('book-detail/<str:slug>/', views.BookDetail, name='book-detail')
]

