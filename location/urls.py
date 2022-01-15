from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('events/', views.event_wrapper, name='events'),
    path('events-detail/<str:slug>/', views.event_detail, name='events-detail'),
]