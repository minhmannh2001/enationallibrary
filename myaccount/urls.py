from django.urls import path
from . import views

app_name = 'my_account'

urlpatterns = [
    path('my_profile/', views.MyProfile.as_view(), name='my_profile'),
    path('my_cart/', views.MyCart.as_view(), name='my_cart'),
    path('my_borrowed_books', views.MyBorrowedBooks.as_view(), name='my_borrowed_books'),
    path('my_plan', views.MyPlan.as_view(), name='my_plan'),
]