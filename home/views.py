from django.shortcuts import render
from django.http import HttpResponse
from category.models import Magazine
from location.models import Event
from category.models import New
from category.models import Book
from category.models import Collection


def home(request):
    print(request.user.customer.all().first().lastName)
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    events = Event.objects.all().order_by('startDate')[0:5]
    top_hot_news = New.objects.all().order_by('-createdAt')[0:1]
    second_hot_news = New.objects.all().order_by('-createdAt')[1:2]
    third_hot_news = New.objects.all().order_by('-createdAt')[2:3]
    top_borrow_books = list(Book.objects.all().order_by('-rating')[0:10])
    top_borrow_books_1 = top_borrow_books[0]
    top_borrow_books_2 = top_borrow_books[1]
    top_borrow_books_3 = top_borrow_books[2]
    top_borrow_books_4 = top_borrow_books[3]
    top_borrow_books_5 = top_borrow_books[4]
    top_borrow_books_6 = top_borrow_books[5]
    top_borrow_books_7 = top_borrow_books[6]
    top_borrow_books_8 = top_borrow_books[7]
    top_borrow_books_9 = top_borrow_books[8]
    top_borrow_books_10 = top_borrow_books[9]
    new_arrival_books = list(Book.objects.all().order_by('-quantity')[0:10])
    new_arrival_books_1 = new_arrival_books[0]
    new_arrival_books_2 = new_arrival_books[1]
    new_arrival_books_3 = new_arrival_books[2]
    new_arrival_books_4 = new_arrival_books[3]
    new_arrival_books_5 = new_arrival_books[4]
    new_arrival_books_6 = new_arrival_books[5]
    new_arrival_books_7 = new_arrival_books[6]
    new_arrival_books_8 = new_arrival_books[7]
    new_arrival_books_9 = new_arrival_books[8]
    new_arrival_books_10 = new_arrival_books[9]
    staff_picks = list(Collection.objects.all()[0:2])
    staff_picks_1 = staff_picks[0]
    staff_picks_2 = staff_picks[1]
    return render(request, 'homepage.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'events': events,
        'top_hot_news': top_hot_news,
        'second_hot_news': second_hot_news,
        'third_hot_news': third_hot_news,
        'top_borrow_books_1': top_borrow_books_1,
        'top_borrow_books_2': top_borrow_books_2,
        'top_borrow_books_3': top_borrow_books_3,
        'top_borrow_books_4': top_borrow_books_4,
        'top_borrow_books_5': top_borrow_books_5,
        'top_borrow_books_6': top_borrow_books_6,
        'top_borrow_books_7': top_borrow_books_7,
        'top_borrow_books_8': top_borrow_books_8,
        'top_borrow_books_9': top_borrow_books_9,
        'top_borrow_books_10': top_borrow_books_10,
        'new_arrival_books_1': new_arrival_books_1,
        'new_arrival_books_2': new_arrival_books_2,
        'new_arrival_books_3': new_arrival_books_3,
        'new_arrival_books_4': new_arrival_books_4,
        'new_arrival_books_5': new_arrival_books_5,
        'new_arrival_books_6': new_arrival_books_6,
        'new_arrival_books_7': new_arrival_books_7,
        'new_arrival_books_8': new_arrival_books_8,
        'new_arrival_books_9': new_arrival_books_9,
        'new_arrival_books_10': new_arrival_books_10,
        'staff_picks_1': staff_picks_1,
        'staff_picks_2': staff_picks_2,
    })