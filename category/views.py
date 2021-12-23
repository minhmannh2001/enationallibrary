from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


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