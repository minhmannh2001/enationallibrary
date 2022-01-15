from django.urls import path, include
from . import views

app_name = 'category'

urlpatterns = [
    path('book-detail/<str:slug>/', views.BookDetail, name='book-detail'),
    path('category-wrapper/', views.category_wrapper, name="category_wrapper"),
    path('category-search/', views.category_search, name="category_search"),
    path('category-bestbook/', views.category_bestBook_all, name="category_bestbook_all"),
    path('category-bestbook/<str:slug>', views.category_bestBook, name="category_bestbook"),
    path('category-newarrivals/', views.category_newArrivals_all, name="category_newarrivals_all"),
    path('category-newarrivals/<str:slug>', views.category_newArrivals, name="category_newarrivals"),
    path('category-staffpicks/', views.category_staffPicks_all, name="category_staffpicks_all"),
    path('category-staffpicks/<str:slug>', views.category_staffPicks, name="category_staffpicks"),
    path('category-magazines/<str:slug>', views.category_magazines, name="category_magazines"),
    path('', views.category),
]

