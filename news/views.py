from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from category.models import New, Review
from django.core.paginator import Paginator


# Create your views here.
def newsreviewswrapper(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    top_hot_news = New.objects.all().order_by('-createdAt')[0:1]
    second_hot_news = New.objects.all().order_by('-createdAt')[1:2]
    third_hot_news = New.objects.all().order_by('-createdAt')[2:3]

    new_News = list(New.objects.all().order_by('-createdAt')[0:10])
    new_News_1 = new_News[0]
    new_News_2 = new_News[1]
    new_News_3 = new_News[2]
    new_News_4 = new_News[3]
    new_News_5 = new_News[4]
    new_News_6 = new_News[5]
    new_News_7 = new_News[6]
    new_News_8 = new_News[7]
    new_News_9 = new_News[8]
    new_News_10 = new_News[9]

    new_Reviews = list(Review.objects.all().order_by('-createdAt')[0:10])
    new_Reviews_1 = new_Reviews[0]
    new_Reviews_2 = new_Reviews[1]
    new_Reviews_3 = new_Reviews[2]
    new_Reviews_4 = new_Reviews[3]
    new_Reviews_5 = new_Reviews[4]
    new_Reviews_6 = new_Reviews[5]
    new_Reviews_7 = new_Reviews[6]
    new_Reviews_8 = new_Reviews[7]
    new_Reviews_9 = new_Reviews[8]
    new_Reviews_10 = new_Reviews[9]

    return render(request, 'news/news-reviews-wrapper.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'top_hot_news': top_hot_news,
        'second_hot_news': second_hot_news,
        'third_hot_news': third_hot_news,
        'new_News_1': new_News_1,
        'new_News_2': new_News_2,
        'new_News_3': new_News_3,
        'new_News_4': new_News_4,
        'new_News_5': new_News_5,
        'new_News_6': new_News_6,
        'new_News_7': new_News_7,
        'new_News_8': new_News_8,
        'new_News_9': new_News_9,
        'new_News_10': new_News_10,
        'new_Reviews_1': new_Reviews_1,
        'new_Reviews_2': new_Reviews_2,
        'new_Reviews_3': new_Reviews_3,
        'new_Reviews_4': new_Reviews_4,
        'new_Reviews_5': new_Reviews_5,
        'new_Reviews_6': new_Reviews_6,
        'new_Reviews_7': new_Reviews_7,
        'new_Reviews_8': new_Reviews_8,
        'new_Reviews_9': new_Reviews_9,
        'new_Reviews_10': new_Reviews_10,
    })


def news(request, pagenum):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    new_News = list(New.objects.all().order_by('-createdAt'))

    numberOfPages = 0
    if len(new_News) % 10 == 0:
        numberOfPages = (len(new_News) - 1) // 10 + 1
    else:
        numberOfPages = len(new_News) // 10 + 1
    numberOfPages = [i for i in range(numberOfPages)]

    pagenum = int(pagenum)
    page_index1 = 0 + 10 * (pagenum - 1)
    page_index2 = 1 + 10 * (pagenum - 1)
    page_index3 = 2 + 10 * (pagenum - 1)
    page_index4 = 3 + 10 * (pagenum - 1)
    page_index5 = 4 + 10 * (pagenum - 1)
    page_index6 = 5 + 10 * (pagenum - 1)
    page_index7 = 6 + 10 * (pagenum - 1)
    page_index8 = 7 + 10 * (pagenum - 1)
    page_index9 = 8 + 10 * (pagenum - 1)
    page_index10 = 9 + 10 * (pagenum - 1)

    new_News_1 = None
    new_News_2 = None
    new_News_3 = None
    new_News_4 = None
    new_News_5 = None
    new_News_6 = None
    new_News_7 = None
    new_News_8 = None
    new_News_9 = None
    new_News_10 = None

    try:
        new_News_1 = new_News[page_index1]
        new_News_2 = new_News[page_index2]
        new_News_3 = new_News[page_index3]
        new_News_4 = new_News[page_index4]
        new_News_5 = new_News[page_index5]
        new_News_6 = new_News[page_index6]
        new_News_7 = new_News[page_index7]
        new_News_8 = new_News[page_index8]
        new_News_9 = new_News[page_index9]
        new_News_10 = new_News[page_index10]

        return render(request, 'news/news.html', {
            'is_login': is_login,
            'is_staff': is_staff,
            'user': request.user,
            'numberOfPages': numberOfPages,
            'new_News_1': new_News_1,
            'new_News_2': new_News_2,
            'new_News_3': new_News_3,
            'new_News_4': new_News_4,
            'new_News_5': new_News_5,
            'new_News_6': new_News_6,
            'new_News_7': new_News_7,
            'new_News_8': new_News_8,
            'new_News_9': new_News_9,
            'new_News_10': new_News_10,
        })
    except IndexError:
        return render(request, 'news/news.html', {
            'is_login': is_login,
            'is_staff': is_staff,
            'user': request.user,
            'numberOfPages': numberOfPages,
            'new_News_1': new_News_1,
            'new_News_2': new_News_2,
            'new_News_3': new_News_3,
            'new_News_4': new_News_4,
            'new_News_5': new_News_5,
            'new_News_6': new_News_6,
            'new_News_7': new_News_7,
            'new_News_8': new_News_8,
            'new_News_9': new_News_9,
            'new_News_10': new_News_10,
        })


def reviews(request, pagenum):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    new_Reviews = list(Review.objects.all().order_by('-createdAt'))

    numberOfPages = 0
    if len(new_Reviews) % 10 == 0:
        numberOfPages = (len(new_Reviews) - 1) // 10 + 1
    else:
        numberOfPages = len(new_Reviews) // 10 + 1
    numberOfPages = [i for i in range(numberOfPages)]

    pagenum = int(pagenum)
    page_index1 = 0 + 10 * (pagenum - 1)
    page_index2 = 1 + 10 * (pagenum - 1)
    page_index3 = 2 + 10 * (pagenum - 1)
    page_index4 = 3 + 10 * (pagenum - 1)
    page_index5 = 4 + 10 * (pagenum - 1)
    page_index6 = 5 + 10 * (pagenum - 1)
    page_index7 = 6 + 10 * (pagenum - 1)
    page_index8 = 7 + 10 * (pagenum - 1)
    page_index9 = 8 + 10 * (pagenum - 1)
    page_index10 = 9 + 10 * (pagenum - 1)

    new_Reviews_1 = None
    new_Reviews_2 = None
    new_Reviews_3 = None
    new_Reviews_4 = None
    new_Reviews_5 = None
    new_Reviews_6 = None
    new_Reviews_7 = None
    new_Reviews_8 = None
    new_Reviews_9 = None
    new_Reviews_10 = None

    try:
        new_Reviews_1 = new_Reviews[page_index1]
        new_Reviews_2 = new_Reviews[page_index2]
        new_Reviews_3 = new_Reviews[page_index3]
        new_Reviews_4 = new_Reviews[page_index4]
        new_Reviews_5 = new_Reviews[page_index5]
        new_Reviews_6 = new_Reviews[page_index6]
        new_Reviews_7 = new_Reviews[page_index7]
        new_Reviews_8 = new_Reviews[page_index8]
        new_Reviews_9 = new_Reviews[page_index9]
        new_Reviews_10 = new_Reviews[page_index10]

        return render(request, 'news/reviews.html', {
            'is_login': is_login,
            'is_staff': is_staff,
            'user': request.user,
            'numberOfPages': numberOfPages,
            'new_Reviews_1': new_Reviews_1,
            'new_Reviews_2': new_Reviews_2,
            'new_Reviews_3': new_Reviews_3,
            'new_Reviews_4': new_Reviews_4,
            'new_Reviews_5': new_Reviews_5,
            'new_Reviews_6': new_Reviews_6,
            'new_Reviews_7': new_Reviews_7,
            'new_Reviews_8': new_Reviews_8,
            'new_Reviews_9': new_Reviews_9,
            'new_Reviews_10': new_Reviews_10,
        })
    except IndexError:
        return render(request, 'news/reviews.html', {
            'is_login': is_login,
            'is_staff': is_staff,
            'user': request.user,
            'numberOfPages': numberOfPages,
            'new_Reviews_1': new_Reviews_1,
            'new_Reviews_2': new_Reviews_2,
            'new_Reviews_3': new_Reviews_3,
            'new_Reviews_4': new_Reviews_4,
            'new_Reviews_5': new_Reviews_5,
            'new_Reviews_6': new_Reviews_6,
            'new_Reviews_7': new_Reviews_7,
            'new_Reviews_8': new_Reviews_8,
            'new_Reviews_9': new_Reviews_9,
            'new_Reviews_10': new_Reviews_10,
        })


def newsdetail(request, slug=None):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    new = New.objects.get(slug=slug)

    news = list(New.objects.all().order_by('?')[0:10])
    news_1 = news[0]
    news_2 = news[1]
    news_3 = news[2]
    news_4 = news[3]
    news_5 = news[4]
    news_6 = news[5]
    news_7 = news[6]
    news_8 = news[7]
    news_9 = news[8]
    news_10 = news[9]
    context = {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'new': new,
        'news_1': news_1,
        'news_2': news_2,
        'news_3': news_3,
        'news_4': news_4,
        'news_5': news_5,
        'news_6': news_6,
        'news_7': news_7,
        'news_8': news_8,
        'news_9': news_9,
        'news_10': news_10,
    }
    return render(request, 'news/news-detail.html', context)


def reviewsdetail(request, slug=None):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    review = Review.objects.get(slug=slug)

    reviews = list(Review.objects.all().order_by('?')[0:10])
    reviews_1 = reviews[0]
    reviews_2 = reviews[1]
    reviews_3 = reviews[2]
    reviews_4 = reviews[3]
    reviews_5 = reviews[4]
    reviews_6 = reviews[5]
    reviews_7 = reviews[6]
    reviews_8 = reviews[7]
    reviews_9 = reviews[8]
    reviews_10 = reviews[9]
    context = {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'review': review,
        'reviews_1': reviews_1,
        'reviews_2': reviews_2,
        'reviews_3': reviews_3,
        'reviews_4': reviews_4,
        'reviews_5': reviews_5,
        'reviews_6': reviews_6,
        'reviews_7': reviews_7,
        'reviews_8': reviews_8,
        'reviews_9': reviews_9,
        'reviews_10': reviews_10,
    }
    return render(request, 'news/reviews-detail.html', context)


