from django.urls import path, include
from . import views

app_name = 'support'

urlpatterns = [
    path('hour-location/', views.hour_location, name='hour_location'),
    path('support-catalog/', views.support_catalog, name='support_catalog'),
    path('support-contactUs/', views.support_contactUs, name='support_contactUs'),
    path('support-libraryFees/', views.support_libraryFees, name='support_libraryFees'),
    path('support-renewals/', views.support_renewals, name='support_renewals'),
    path('support-wrapper/', views.support_wrapper, name='support_wrapper'),
    path('support-card/', views.support_card, name='support_card'),
]

