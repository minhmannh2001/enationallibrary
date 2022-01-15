from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Magazine, Collection
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
import html
import math
from django.utils import timezone
from datetime import timedelta


def BookDetail(request, slug):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    book = Book.objects.get(slug=slug)
    genre = book.genre
    author = book.author.first()
    same_genre_books = list(Book.objects.filter(genre=genre))
    same_genre_books_lt_6 = len(same_genre_books) > 6
    same_author_books = list(Book.objects.filter(author=author))
    same_author_books_lt_6 = len(same_author_books) > 6
    return render(request, 'category/book_detail.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'book': book,
        'same_genre_books_lt_6': same_genre_books_lt_6,
        'same_genre_books': same_genre_books,
        'same_author_books_lt_6': same_author_books_lt_6,
        'same_author_books': same_author_books,
    })


def category(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    book_list = Book.objects.all().order_by('title')
    trang = int(request.GET.get('trang', 1))
    total_page = math.ceil(len(book_list)/10)
    results = [ob.as_json() for ob in book_list]
    data = json.dumps(results, ensure_ascii=False)
    return render(request, 'category/category_search.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'data': data,
        'total_page':range(1, total_page+1),
        'number_total_page':total_page,
        'page': trang
    })


@csrf_exempt
def category_search(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    keyStr = request.POST.get('content_key', '')
    if keyStr == '':
        keyStr = request.GET.get('keyStr', '')
    book_list_title = Book.objects.filter(title__icontains=keyStr)
    book_list_author = Book.objects.filter(author__name__icontains=keyStr)
    book_list = list(book_list_title)
    book_list.extend(x for x in book_list_author if x not in book_list)
    trang = int(request.GET.get('trang', 1))

    p = Paginator(book_list, 10)
    try:
        good_list = p.page(trang)
    except PageNotAnInteger:
        good_list = p.page(1)
    except EmptyPage:
        good_list = p.page(p.num_pages)
    total_page = math.ceil(len(book_list)/10)
    results = [ob.as_json() for ob in book_list]
    data = json.dumps(results, ensure_ascii=False)
    return render(request, 'category/category_search.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'good_lists': good_list,
        'keyStr': keyStr,
        'data': data,
        'total_page':range(1, total_page+1),
        'number_total_page':total_page,
        'page': trang
    })


def category_wrapper(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'category/category-wrapper.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
    })


def category_bestBook_all(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    genreFitler = [i[0] for i in Book.bookGenre]
    books = Book.objects.all()
    has_slug = False
    publishYear = request.GET.get('publish-year')
    if publishYear == 'None':
        publishYear = None
    is2021 = False
    is2020 = False
    is2019 = False
    is2018 = False
    isNone = True
    has_slug = False
    if publishYear is not None:
        books = books.filter(publishYear__year=publishYear)
        if publishYear == '2020':
            is2021 = False
            is2020 = True
            is2019 = False
            is2018 = False
            isNone = False
        if publishYear == '2021':
            is2021 = True
            is2020 = False
            is2019 = False
            is2018 = False
            isNone = False
        if publishYear == '2019':
            is2021 = False
            is2020 = False
            is2019 = True
            is2018 = False
            isNone = False
        if publishYear == '2018':
            is2021 = False
            is2020 = False
            is2019 = False
            is2018 = True
            isNone = False
    return render(request, 'category/category-bestBook.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'genreFilter': genreFitler,
        'books': books,
        'has_slug': has_slug,
        'is2021': is2021,
        'is2020': is2020,
        'is2019': is2019,
        'is2018': is2018,
        'isNone': isNone,
    })


def category_bestBook(request, slug):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    genreFitler = [i[0] for i in Book.bookGenre]
    books = Book.objects.all()
    books = books.filter(genre=slug)
    publishYear = request.GET.get('publish-year')
    if publishYear == 'None':
        publishYear = None
    is2021 = False
    is2020 = False
    is2019 = False
    is2018 = False
    isNone = True
    has_slug = True
    if publishYear is not None:
        books = books.filter(publishYear__year=publishYear)
        if publishYear == '2020':
            is2021 = False
            is2020 = True
            is2019 = False
            is2018 = False
            isNone = False
        if publishYear == '2021':
            is2021 = True
            is2020 = False
            is2019 = False
            is2018 = False
            isNone = False
        if publishYear == '2019':
            is2021 = False
            is2020 = False
            is2019 = True
            is2018 = False
            isNone = False
        if publishYear == '2018':
            is2021 = False
            is2020 = False
            is2019 = False
            is2018 = True
            isNone = False
    return render(request, 'category/category-bestBook.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'genreFilter': genreFitler,
        'books': books,
        'slug': slug,
        'is2021': is2021,
        'is2020': is2020,
        'is2019': is2019,
        'is2018': is2018,
        'isNone': isNone,
        'has_slug': has_slug,
    })


def category_magazines(request, slug):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    magazines = Magazine.objects.filter(genre__exact=slug)
    publishYear = request.GET.get('publish-year')
    if publishYear == 'None':
        publishYear = None
    is2021 = False
    is2020 = False
    is2019 = False
    is2018 = False
    isNone = True
    if publishYear is not None:
        magazines = magazines.filter(publishYear__year=publishYear)
        if publishYear == '2020':
            is2021 = False
            is2020 = True
            is2019 = False
            is2018 = False
            isNone = False
        if publishYear == '2021':
            is2021 = True
            is2020 = False
            is2019 = False
            is2018 = False
            isNone = False
        if publishYear == '2019':
            is2021 = False
            is2020 = False
            is2019 = True
            is2018 = False
            isNone = False
        if publishYear == '2018':
            is2021 = False
            is2020 = False
            is2019 = False
            is2018 = True
            isNone = False

    return render(request, 'category/category-magazines.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'magazines': magazines,
        'slug': slug,
        'is2021': is2021,
        'is2020': is2020,
        'is2019': is2019,
        'is2018': is2018,
        'isNone': isNone,
    })


def category_staffPicks_all(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    collections = Collection.objects.all()
    isAllCollections = True
    return render(request, 'category/category-staffPicks.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'collections': collections,
        'isAllCollections': isAllCollections,
    })


def category_staffPicks(request, slug):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    collections = Collection.objects.all()
    collection = collections.get(title=slug)
    isAllCollections = False
    return render(request, 'category/category-staffPicks.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'collections': collections,
        'collection': collection,
        'isAllCollections': isAllCollections,
    })


def category_newArrivals(request, slug):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    genreFitler = [i[0] for i in Book.bookGenre]
    books = Book.objects.all()
    books = books.filter(createdAt__gte=timezone.now() - timedelta(days=30))
    books = books.filter(genre=slug)
    return render(request, 'category/category-newArrivals.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'genreFilter': genreFitler,
        'books': books,
    })


def category_newArrivals_all(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    genreFitler = [i[0] for i in Book.bookGenre]
    books = Book.objects.all()
    books = books.filter(createdAt__gte=timezone.now() - timedelta(days=30))
    return render(request, 'category/category-newArrivals.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'genreFilter': genreFitler,
        'books': books,
    })



