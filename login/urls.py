from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('sign-in/', views.sign_in.as_view(), name='sign-in'),
    path('sign-up/', views.sign_up.as_view(), name='sign-up'),
    path('log-out/', views.log_out, name='log-out'),
]


