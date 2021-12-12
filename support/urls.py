from django.urls import path, include
from . import views

app_name = 'support'

urlpatterns = [
    path('hour-location/', views.hour_location, name='hour_location')
]

