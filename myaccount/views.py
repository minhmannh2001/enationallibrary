from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from .models import MemberCard, Customer, OrderedBooks
from . import models
from flask import request
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views import View
from category.models import Book, Magazine, New
from location.models import Event
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UpdateProfileForm, formOrder, formReturn, updatePlanform, registerPlanform
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from datetime import timedelta
from io import StringIO
from io import BytesIO
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin


class MyProfile(LoginRequiredMixin, View):
    login_url = '/login/require-login/'

    def get(self, request):
        is_login = False
        is_staff = False

        if not request.user.is_anonymous:
            is_login = True
        if request.user.is_staff:
            is_staff = True
        customer = request.user.customer.all().first()
        print(customer)
        hM = False
        if customer.memberCard != None:
            hM = True
        return render(request, 'myaccount/myAccount-profile.html', {
            'is_login': is_login,
            'is_staff': is_staff,
            'user': request.user.customer.all().first(),
            'hM': hM,
        })


@login_required(login_url='/login/require-login/')
def change_profile(request):
    customer = request.user.customer.all().first()
    cP = UpdateProfileForm(initial={'lastName': customer.lastName, 'firstName': customer.firstName,
                                    'dateOfBirth': customer.dateOfBirth,
                                    'address': customer.address,
                                    'city': customer.city,
                                    'gender': customer.gender,
                                    'identificationCard': customer.identificationCard,
                                    'email': customer.emailAddress,
                                    'phoneNumber': customer.phoneNumber})
    return render(request, 'myaccount/changeInfomation.html', {'cP': cP})


@login_required(login_url='/login/require-login/')
def save_profile(request):
    if request.method == 'POST':
        cP = UpdateProfileForm(request.POST)
        if cP.is_valid():
            user = request.user
            customer = user.customer.all().first()
            customer.lastName = cP.cleaned_data['lastName']
            customer.firstName = cP.cleaned_data['firstName']
            customer.dateOfBirth = cP.cleaned_data['dateOfBirth']
            customer.address = cP.cleaned_data['address']
            customer.gender = cP.cleaned_data['gender']
            customer.emailAddress = cP.cleaned_data['city']
            customer.identificationCard = cP.cleaned_data['identificationCard']
            customer.email = cP.cleaned_data['email']
            customer.phoneNumber = cP.cleaned_data['phoneNumber']
            customer.save()
            user.save()
            return HttpResponseRedirect(reverse('myaccount:profile'))
        else:
            is_login = False
            is_staff = False
            if not request.user.is_anonymous:
                is_login = True
            if request.user.is_staff:
                is_staff = True
            return render(request, 'myaccount/changeInfomation.html', {'cP': cP,
                                                                       'is_login': is_login,
                                                                       'is_staff': is_staff, })

    else:
        return HttpResponse('not POST')


@login_required(login_url='/login/require-login/')
def save_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        print(form.cleaned_data['new_password1'])
        if form.is_valid():
            user = form.save()
            user = request.user
            print(form.cleaned_data['new_password1'])
            user.set_password(form.cleaned_data['new_password1'])
            user.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request, 'myAccount-profile.html')
        else:

            return HttpResponse('not Post')
            messages.error(request, 'Please correct the error below.')


class change_password(LoginRequiredMixin, View):
    login_url = '/login/require-login/'

    def get(self, request):
        is_login = False
        is_staff = False
        if not request.user.is_anonymous:
            is_login = True
        if request.user.is_staff:
            is_staff = True
        return render(request, 'myaccount/changePW.html', {
            'is_login': is_login,
            'is_staff': is_staff, })

    def post(self, request):
        is_login = False
        is_staff = False
        if not request.user.is_anonymous:
            is_login = True
        if request.user.is_staff:
            is_staff = True
        user = request.user
        old_password_valid = False
        new_pw_isvalid = False
        new_pw_8 = False
        old_pw_isvalid = False
        new_password_isvalid = False
        is_3 = False
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        print(old_password)
        print(user.check_password(old_password))
        if user.check_password(old_password) == False:
            old_pw_isvalid = True
            return render(request, 'myaccount/changePW.html', {'old_pw_isvalid': old_pw_isvalid,
                                                               'is_login': is_login,
                                                               'is_staff': is_staff, })
        if new_password1 != new_password2:
            new_password_isvalid = True
            return render(request, 'myaccount/changePW.html', {'new_password_isvalid': new_password_isvalid,
                                                               'is_login': is_login,
                                                               'is_staff': is_staff, })
        if len(old_password) == 0:
            old_password_valid = True
            return render(request, 'myaccount/changePW.html', {'old_password_valid': old_password_valid,
                                                               'is_login': is_login,
                                                               'is_staff': is_staff, })
        if len(new_password1) == 0:
            new_pw_isvalid = True
            return render(request, 'myaccount/changePW.html', {'new_pw_isvalid': new_pw_isvalid,
                                                               'is_login': is_login,
                                                               'is_staff': is_staff, })
        if len(new_password1) < 9:
            new_pw_8 = True
            return render(request, 'myaccount/changePW.html', {'new_pw_8': new_pw_8,
                                                               'is_login': is_login,
                                                               'is_staff': is_staff, })
        if new_password1.isalpha() == True or new_password1.isdigit() == True:
            is_3 = True
            return render(request, 'myaccount/changePW.html', {'is_3': is_3,
                                                               'is_login': is_login,
                                                               'is_staff': is_staff, })

        user.set_password(request.POST.get('new_password1'))
        user.save()
        update_session_auth_hash(request, user)
        user.save()
        return redirect('myaccount:profile')


@login_required(login_url='/login/require-login/')
def add_to_cart_view(request, pk):
    customer = request.user.customer.all().first()
    if customer.memberCard == None:
        return HttpResponseRedirect(reverse('myaccount:registerPlan'))
    else:
        memberCard = customer.memberCard
        book = models.Book.objects.get(id=pk)
        memberCard.booksBeingBorrowed.add(book)
        memberCard.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login/require-login/')
def remove_from_cart(request, pk):
    customer = request.user.customer.all().first()
    memberCard = customer.memberCard
    book = models.Book.objects.get(id=pk)
    memberCard.booksBeingBorrowed.remove(book)
    memberCard.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login/require-login/')
def cart_view(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    customer = request.user.customer.all().first()
    memberCard = customer.memberCard
    hM = False
    if customer.memberCard != None:
        hM = True
    else:
        return HttpResponseRedirect(reverse('myaccount:registerPlan'))
    is_HN = False
    if customer.city == 'Hà Nội':
        is_HN = True
    else:
        is_HN = False
    is_over_book = False
    max_book = memberCard.maxNbOfBooksToBorrow - memberCard.nbOfBooksBeingBorrowed
    fO = formOrder(initial={'name': customer.firstName, 'address': customer.address,
                            'city': customer.city,
                            'phoneNumber': customer.phoneNumber})
    customer = request.user.customer.all().first()
    memberCard = customer.memberCard
    books = memberCard.booksBeingBorrowed.all()
    is_V = False
    is_F = False
    if books == None:
        is_F = True
    book_count_in_cart = len(books)
    if book_count_in_cart == 0:
        is_F = True
    if book_count_in_cart > max_book:
        is_over_book = True
        is_F = True
    is_B = False
    if memberCard.servicePlan == 'MB' or memberCard.servicePlan == 'AB':
        is_B = True
        if books != None:
            for book in books:
                if book.isRare == True:
                    is_V = True
                    is_F = True
    if books != None:
        for book in books:
            if book.quantity <= book.beingBorrowedQuantity:
                is_F = True
    return render(request, 'myaccount/myAccount-myCart.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'books': books,
        'book_count_in_cart': book_count_in_cart,
        'is_over_book': is_over_book,
        'max_book': max_book,
        'is_HN': is_HN,
        'is_V': is_V,
        'is_F': is_F,
        'is_B': is_B,
        'fO': fO,
        'hM': hM, })


@login_required(login_url='/login/require-login/')
def cart_payment(request):
    if request.method == 'POST':
        fO = formOrder(request.POST)
        if fO.is_valid():
            is_login = False
            is_staff = False
            if not request.user.is_anonymous:
                is_login = True
            if request.user.is_staff:
                is_staff = True
            customer = request.user.customer.all().first()
            uP = updatePlanform()
            name = fO.cleaned_data['name']
            address = fO.cleaned_data['address']
            city = fO.cleaned_data['city']
            return render(request, 'myaccount/cart-payment.html', {
                'is_login': is_login,
                'is_staff': is_staff,
                'user': request.user.customer.all().first(),
                'name': name,
                'address': address,
                'city': city,
                'uP': uP,
            })
        else:
            is_login = False
            is_staff = False
            if not request.user.is_anonymous:
                is_login = True
            if request.user.is_staff:
                is_staff = True
            customer = request.user.customer.all().first()
            memberCard = customer.memberCard
            hM = False
            if customer.memberCard != None:
                hM = True
            is_HN = False
            if customer.city == 'Hà Nội':
                is_HN = True
            else:
                is_HN = False
            is_over_book = False
            max_book = memberCard.maxNbOfBooksToBorrow - memberCard.nbOfBooksBeingBorrowed
            fO = formOrder(initial={'name': customer.firstName, 'address': customer.address,
                                    'city': customer.city,
                                    'phoneNumber': customer.phoneNumber})
            customer = request.user.customer.all().first()
            memberCard = customer.memberCard
            books = memberCard.booksBeingBorrowed.all()
            is_V = False
            is_F = False
            if books == None:
                is_F = True
            book_count_in_cart = len(books)
            if book_count_in_cart == 0:
                is_F = True
            if book_count_in_cart > max_book:
                is_over_book = True
                is_F = True
            is_B = False
            if memberCard.servicePlan == 'MB' or memberCard.servicePlan == 'AB':
                is_B = True
                if books != None:
                    for book in books:
                        if book.isRare == True:
                            is_V = True
                            is_F = True
            if books != None:
                for book in books:
                    if book.quantity <= book.beingBorrowedQuantity:
                        is_F = True
            return render(request, 'myaccount/myAccount-myCart.html', {
                'is_login': is_login,
                'is_staff': is_staff,
                'books': books,
                'book_count_in_cart': book_count_in_cart,
                'is_over_book': is_over_book,
                'max_book': max_book,
                'is_HN': is_HN,
                'is_V': is_V,
                'is_F': is_F,
                'is_B': is_B,
                'fO': fO,
                'hM': hM})


@login_required(login_url='/login/require-login/')
def newOrder(request, name, address, city):
    if request.method == 'POST':
        uP = updatePlanform(request.POST)
        if uP.is_valid():
            customer = request.user.customer.all().first()
            memberCard = customer.memberCard
            books = memberCard.booksBeingBorrowed.all()
            for book in books:
                if customer.memberCard == None:
                    return render(request, 'myaccount/myAccount-updatePlan.html')
                t1 = timedelta(days=45)
                if customer.memberCard.servicePlan == 'AV' or customer.memberCard.servicePlan == 'MV':
                    t1 = timedelta(days=60)
                t2 = date.today()
                t3 = t2 + t1
                m = customer.memberCard.nbOfBooksBeingBorrowed + 1
                customer.memberCard.nbOfBooksBeingBorrowed = m
                customer.memberCard.save()
                m = book.beingBorrowedQuantity + 1
                book.beingBorrowedQuantity = m
                book.save()
                OrderedBooks.objects.create(
                    book=book,
                    customer=customer,
                    ordered_date=date.today(),
                    expired_date=t3,
                    return_date=t3,
                    status='Bình thường')
                memberCard.booksBeingBorrowed.remove(book)
            return HttpResponseRedirect(reverse('myaccount:borrowBooks'))
        else:
            customer = request.user.customer.all().first()
            return render(request, 'myaccount/cart-payment.html', {
                'name': name,
                'address': address,
                'city': city,
                'uP': uP,
            })

    else:
        return HttpResponse('NOT POST')


class MyBorrowedBooks(LoginRequiredMixin, View):
    login_url = '/login/require-login/'

    def get(self, request):
        is_login = False
        is_staff = False
        if not request.user.is_anonymous:
            is_login = True
        if request.user.is_staff:
            is_staff = True
        user = request.user
        customer = user.customer.all().first()
        hM = False
        if customer.memberCard != None:
            hM = True
        myOrder = OrderedBooks.objects.filter(customer=customer).order_by('-expired_date')
        count = len(myOrder)
        today = date.today()
        return render(request, 'myaccount/myAccount-borrowBooks.html', {
            'customer': customer,
            'myOrder': myOrder,
            'count': count,
            'today': today,
            'is_login': is_login,
            'is_staff': is_staff,
            'hM': hM,
        })


@login_required(login_url='/login/require-login/')
def returnBook(request, orderID, bookID):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    hM = False
    customer = request.user.customer.all().first()
    if customer.memberCard != None:
        hM = True
    customer = request.user.customer.all().first()
    order = models.OrderedBooks.objects.filter(id=orderID).all().first()
    book = models.Book.objects.get(id=bookID)
    rB = formReturn(initial={'lastName': customer.lastName, 'firstName': customer.firstName, 'numberOfbook': bookID,
                             'bookName': book})
    return render(request, 'myaccount/returnBooks.html', {'rB': rB,
                                                          'bookID': bookID,
                                                          'orderID': orderID,
                                                          'is_login': is_login,
                                                          'is_staff': is_staff,
                                                          'hM': hM,
                                                          })


@login_required(login_url='/login/require-login/')
def saveReturnBook(request, orderID, bookID):
    if request.method == 'POST':
        rB = formReturn(request.POST, request.FILES)
        if rB.is_valid():
            customer = request.user.customer.all().first()
            order = models.OrderedBooks.objects.filter(id=orderID).all().first()
            m = customer.memberCard.nbOfBooksBeingBorrowed - 1
            customer.memberCard.nbOfBooksBeingBorrowed = m
            customer.memberCard.save()
            book = models.Book.objects.get(id=bookID)
            order.status = 'Đã trả'
            order.return_date = date.today()
            order.save()
            quantity1 = book.beingBorrowedQuantity - 1
            book.beingBorrowedQuantity = quantity1
            book.save()
            """n=customer.memberCard.nbOfBooksBeingBorrowed + 1
            customer.memberCard.nbOfBooksBeingBorrowed = n
            customer.memberCard.save()"""
            return HttpResponseRedirect(reverse('myaccount:borrowBooks'))
        else:
            is_login = False
            is_staff = False
            if not request.user.is_anonymous:
                is_login = True
            if request.user.is_staff:
                is_staff = True
            return render(request, 'myaccount/returnBooks.html', {'rB': rB,
                                                                  'bookID': bookID,
                                                                  'orderID': orderID,
                                                                  'is_login': is_login,
                                                                  'is_staff': is_staff, })
    else:
        return HttpResponse('not POST')


import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def download_invoice_view(request, orderID, bookID):
    customer = request.user.customer.all().first()
    order = models.OrderedBooks.objects.filter(id=orderID).all().first()
    book = models.Book.objects.get(id=bookID)
    mydict = {
        # 'ordered_date':order.ordered_date,
        'customer_name': order.customer,
        'customer_email': customer.emailAddress,
        'ordered_phone': customer.phoneNumber,
        'order_status': order.status,
        'book_name': book.title,
        'order': order,
    }
    return render_to_pdf('myaccount/download_invoice.html', mydict)


class MyPlan(LoginRequiredMixin, View):
    login_url = '/login/require-login/'

    def get(self, request):
        is_login = False
        is_staff = False
        if not request.user.is_anonymous:
            is_login = True
        if request.user.is_staff:
            is_staff = True
        is_none_membercard = False
        is_B = False
        is_V = False
        is_MB = False
        is_AB = False
        is_MV = False
        is_AV = False
        user = request.user
        customer = user.customer.all().first()
        hM = False
        if customer.memberCard != None:
            hM = True
        SMB = 200.000
        SAB = 100.000
        SMV = 400.000
        SAV = 240.000
        events = Event.objects.all()
        today = date.today()
        if events != None:
            max = 0
            for event in events:
                startDate = datetime.date(event.startDate)
                endDate = datetime.date(event.endDate)
                if today >= startDate and today <= endDate:
                    if max < event.discountFactor:
                        max = event.discountFactor
            m = SMB - SMB * max / 100
            SMB = m
            m = SAB - SAB * max / 100
            SAB = m
            m = SMV - SMV * max / 100
            SMV = m
            m = SAV - SAV * max / 100
            SAV = m
        SAB1 = 12 * SAB
        SAV1 = 12 * SAV
        SAB2 = 3 * SMB
        SAV2 = 3 * SMV
        if customer.firstName == None or customer.lastName == None or customer.address == None or customer.city == None or customer.emailAddress == None:
            return HttpResponseRedirect(reverse('myaccount:registerPlan'))
        myPlan = customer.memberCard
        if customer.memberCard == None:
            is_none_membercard = True
        else:
            if customer.memberCard.servicePlan == 'MB':
                is_MB = True
                is_B = True
            if customer.memberCard.servicePlan == 'AB':
                is_AB = True
                is_B = True
            if customer.memberCard.servicePlan == 'MV':
                is_MV = True
                is_V = True
            if customer.memberCard.servicePlan == 'AV':
                is_AV = True
                is_V = True

        return render(request, 'myaccount/myAccount-updatePlan.html', {
            'user': request.user,
            'myPlan': myPlan,
            'customer': customer,
            'is_none_membercard': is_none_membercard,
            'is_MB': is_MB,
            'is_MV': is_MV,
            'is_AB': is_AB,
            'is_AV': is_AV,
            'is_B': is_B,
            'is_V': is_V,
            'is_login': is_login,
            'is_staff': is_staff,
            'SMB': SMB,
            'SAB': SAB,
            'SMV': SMV,
            'SAV': SAV,
            'SAV1': SAV1,
            'SAB1': SAB1,
            'SAV2': SAV2,
            'SAB2': SAB2,
            'hM': hM,
        })


@login_required(login_url='/login/require-login/')
def formUpdate(request, number):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    print(number)
    uP = updatePlanform()
    return render(request, 'myaccount/register-payment.html', {
            'is_login': is_login,
            'is_staff': is_staff,
            'user': request.user.customer.all().first(),'uP': uP, 'number': number})


@login_required(login_url='/login/require-login/')
def updatePlan(request, number):
    if request.method == 'POST':
        uP = updatePlanform(request.POST)
        if uP.is_valid():
            customer = request.user.customer.all().first()
            is_login = False
            is_staff = False
            if not request.user.is_anonymous:
                is_login = True
            if request.user.is_staff:
                is_staff = True
            if number == 1:
                if customer.memberCard == None:
                    memberCard = MemberCard.objects.create(servicePlan='MB', numOfFault=0, maxNbOfBooksToBorrow=5,
                                                           nbOfBooksBeingBorrowed=0, registerDate=date.today(),
                                                           expriedDate=date.today() + timedelta(days=30))
                    customer.memberCard = memberCard;
                    customer.memberCard.save()
                    customer.save()
                #    return HttpResponse('success')
                if customer.memberCard.servicePlan == 'MB':
                    m = customer.memberCard.expriedDate + timedelta(days=30)
                    customer.memberCard.expriedDate = m
                    customer.memberCard.maxNbOfBooksToBorrow = 5
                    customer.memberCard.save()
                #    return HttpResponse('success')

                if customer.memberCard.servicePlan == 'AB':
                    m = customer.memberCard.expriedDate + timedelta(days=30)
                    customer.memberCard.expriedDate = m
                    customer.memberCard.maxNbOfBooksToBorrow = 5
                    customer.memberCard.save()
                #    return HttpResponse('success')

                if customer.memberCard.servicePlan == 'MV':
                    customer.memberCard.servicePlan = 'MB'
                    m = customer.memberCard.expriedDate + timedelta(days=30)
                    customer.memberCard.expriedDate = m
                    customer.memberCard.maxNbOfBooksToBorrow = 5
                    customer.memberCard.save()
                #    return HttpResponse('success')
                if customer.memberCard.servicePlan == 'AV':
                    customer.memberCard.servicePlan = 'MB'
                    m = customer.memberCard.expriedDate + timedelta(days=30)
                    customer.memberCard.expriedDate = m
                    customer.memberCard.maxNbOfBooksToBorrow = 5
                    customer.memberCard.save()
                #    return HttpResponse('success')
            if number == 3:
                if customer.memberCard == None:
                    memberCard = MemberCard.objects.create(servicePlan='MV', numOfFault=0, maxNbOfBooksToBorrow=8,
                                                           nbOfBooksBeingBorrowed=0, registerDate=date.today(),
                                                           expriedDate=date.today() + timedelta(days=30))
                    customer.memberCard = memberCard;
                    customer.memberCard.save()
                    customer.save()
                #   return HttpResponse('success')
                if customer.memberCard.servicePlan == 'MB':
                    customer.memberCard.servicePlan = 'MV'
                    customer.memberCard.registerDate = date.today()
                    customer.memberCard.expriedDate = date.today() + timedelta(days=30)
                    customer.memberCard.maxNbOfBooksToBorrow = 8
                    customer.memberCard.save()
                #   return HttpResponse('success')
                if customer.memberCard.servicePlan == 'AB':
                    customer.memberCard.servicePlan = 'MV'
                    customer.memberCard.registerDate = date.today()
                    customer.memberCard.expriedDate = date.today() + timedelta(days=30)
                    customer.memberCard.maxNbOfBooksToBorrow = 8
                    customer.memberCard.save()
                #    return HttpResponse('success')
                if customer.memberCard.servicePlan == 'MV':
                    m = customer.memberCard.expriedDate + timedelta(days=30)
                    customer.memberCard.maxNbOfBooksToBorrow = 8
                    customer.memberCard.expriedDate = m
                    customer.memberCard.save()
                #   return HttpResponse('success')
                if customer.memberCard.servicePlan == 'AV':
                    customer.memberCard.servicePlan = 'MV'
                    m = customer.memberCard.expriedDate + timedelta(days=30)
                    customer.memberCard.maxNbOfBooksToBorrow = 8
                    customer.memberCard.expriedDate = m
                    customer.memberCard.save()
            #    return HttpResponse('success')
            if number == 2:
                if customer.memberCard == None:
                    memberCard = MemberCard.objects.create(servicePlan='AB', numOfFault=0, maxNbOfBooksToBorrow=5,
                                                           nbOfBooksBeingBorrowed=0, registerDate=date.today(),
                                                           expriedDate=date.today() + timedelta(days=365))
                    customer.memberCard = memberCard;
                    customer.memberCard.save()
                    customer.save()
                #    return HttpResponse('success')
                if customer.memberCard.servicePlan == 'MB':
                    customer.memberCard.servicePlan = 'AB'
                    m = customer.memberCard.expriedDate + timedelta(days=365)
                    customer.memberCard.maxNbOfBooksToBorrow = 5
                    customer.memberCard.expriedDate = m
                    customer.memberCard.save()
                #   return HttpResponse('success')

                if customer.memberCard.servicePlan == 'AB':
                    m = customer.memberCard.expriedDate + timedelta(days=365)
                    customer.memberCard.expriedDate = m
                    customer.memberCard.maxNbOfBooksToBorrow = 5
                    customer.memberCard.save()
                #    return HttpResponse('success')

                if customer.memberCard.servicePlan == 'MV':
                    customer.memberCard.servicePlan = 'AM'
                    m = customer.memberCard.expriedDate + timedelta(days=365)
                    customer.memberCard.expriedDate = m
                    customer.memberCard.maxNbOfBooksToBorrow = 5
                    customer.memberCard.save()
                #    return HttpResponse('success')
                if customer.memberCard.servicePlan == 'AV':
                    m = customer.memberCard.expriedDate + timedelta(days=365)
                    customer.memberCard.expriedDate = m
                    customer.memberCard.maxNbOfBooksToBorrow = 5
                    customer.memberCard.save()
                #   return HttpResponse('success')
            if number == 4:

                if customer.memberCard == None:
                    memberCard = MemberCard.objects.create(servicePlan='AV', numOfFault=0, maxNbOfBooksToBorrow=8,
                                                           nbOfBooksBeingBorrowed=0, registerDate=date.today(),
                                                           expriedDate=date.today() + timedelta(years=1))
                    customer.memberCard = memberCard;
                    customer.memberCard.save()
                    customer.save()
                #    return HttpResponse('success')
                if customer.memberCard.servicePlan == 'MB':
                    customer.memberCard.servicePlan = 'AV'
                    customer.memberCard.registerDate = date.today()
                    customer.memberCard.expriedDate = date.today + timedelta(days=365)
                    customer.memberCard.maxNbOfBooksToBorrow = 8
                    customer.memberCard.save()
                #   return HttpResponse('success')

                if customer.memberCard.servicePlan == 'AB':
                    customer.memberCard.servicePlan = 'AV'
                    customer.memberCard.registerDate = date.today()
                    customer.memberCard.expriedDate = date.today + timedelta(days=30)
                    customer.memberCard.maxNbOfBooksToBorrow = 8
                    customer.memberCard.save()
                #    return HttpResponse('success')

                if customer.memberCard.servicePlan == 'MV':
                    customer.memberCard.servicePlan = 'AV'
                    m = customer.memberCard.expriedDate + timedelta(days=365)
                    customer.memberCard.expriedDate = m
                    customer.memberCard.maxNbOfBooksToBorrow = 8
                    customer.memberCard.save()
                #    return HttpResponse('success')
                if customer.memberCard.servicePlan == 'AV':
                    m = customer.memberCard.expriedDate + timedelta(days=365)
                    customer.memberCard.expriedDate = m
                    customer.memberCard.maxNbOfBooksToBorrow = 8
                    customer.memberCard.save()
                #    return HttpResponse('success')

            return render(request, 'myaccount/getACard3.html', {'memberCard': customer.memberCard, 'customer': customer,
                                                                'is_login': is_login,
                                                                'is_staff': is_staff, })
        else:
            return render(request, 'myaccount/register-payment.html', {'uP': uP, 'number': number})
    else:
        return HttpResponse('no is_valid')


@login_required(login_url='/login/require-login/')
def viewmycard(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    customer = request.user.customer.all().first()
    if customer.memberCard == None:
        return render(request, 'myaccount/getACard1.html')
    memberCard = customer.memberCard
    return render(request, 'myaccount/my_Card.html', {'memberCard': memberCard,
                                                      'customer': customer,
                                                      'is_login': is_login,
                                                      'is_staff': is_staff,
                                                      })


def enationallibrary(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'myaccount/getACard1.html', {
        'is_login': is_login,
        'is_staff': is_staff,
    })


@login_required(login_url='/login/require-login/')
def enationallibrary1(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    customer = request.user.customer.all().first()
    rpf = registerPlanform(initial={'lastName': customer.lastName,
                                    'firstName': customer.firstName,
                                    'dateOfBirth': customer.dateOfBirth,
                                    'email': customer.emailAddress,
                                    'address': customer.address,
                                    'city': customer.city,
                                    'identificationCard': customer.identificationCard,
                                    'phoneNumber': customer.phoneNumber,
                                    'gender': customer.gender,
                                    })
    return render(request, 'myaccount/getACard2.html', {'rpf': rpf,
                                                        'is_login': is_login,
                                                        'is_staff': is_staff, })


@login_required(login_url='/login/require-login/')
def enationallibrary2(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'myaccount/getACard3.html',
                  {'is_login': is_login,
                   'is_staff': is_staff, })


@login_required(login_url='/login/require-login/')
def save_profile_plan(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    if request.method == 'POST':
        rpf = registerPlanform(request.POST)
        print(rpf.errors)
        if rpf.is_valid():
            user = request.user
            customer = user.customer.all().first()
            customer.lastName = rpf.cleaned_data['lastName']
            customer.firstName = rpf.cleaned_data['firstName']
            customer.dateOfBirth = rpf.cleaned_data['dateOfBirth']
            customer.address = rpf.cleaned_data['address']
            customer.gender = rpf.cleaned_data['gender']
            customer.city = rpf.cleaned_data['city']
            customer.identificationCard = rpf.cleaned_data['identificationCard']
            customer.emailAddress = rpf.cleaned_data['email']
            customer.phoneNumber = rpf.cleaned_data['phoneNumber']
            customer.save()
            user.save()
            return HttpResponseRedirect(reverse('myaccount:my_plan'))
        else:
            dict = {'rpf': rpf,
                    'is_login': is_login,
                    'is_staff': is_staff, }
            return render(request, 'myaccount/getACard2.html', {'rpf': rpf,
                                                                'is_login': is_login,
                                                                'is_staff': is_staff, })
    else:
        return HttpResponse('not POST')








