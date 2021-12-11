from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up.as_view(), name='sign-up'),
    path('email-verification/', views.email_verification, name='email-verification'),
    path('reset-password/', views.reset_password, name='reset-password'),
]