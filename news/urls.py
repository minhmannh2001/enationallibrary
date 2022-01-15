from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('news-reviews-wrapper/',views.newsreviewswrapper, name='news-reviews-wrapper'),
    path('news/<str:pagenum>/',views.news, name='news'),
    path('reviews/<str:pagenum>/',views.reviews, name='reviews'),
    path('news/news-detail/<slug:slug>/',views.newsdetail, name='news-detail'),
    path('reviews/reviews-detail/<slug:slug>/',views.reviewsdetail, name='reviews-detail'),
]


