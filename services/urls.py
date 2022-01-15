from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('services-wrapper/', views.services_wrapper, name='services_wrapper'),
    path('services-pickup/', views.services_pickup, name='services_pickup'),
    path('services-reserveRoom/', views.services_reserveRoom, name='services_reserveRoom'),
    path('services-historyRoom/', views.services_historyRoom, name='services_historyRoom'),
]