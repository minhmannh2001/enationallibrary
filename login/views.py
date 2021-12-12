from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from myaccount.models import Customer


class sign_in(View):
    def get(self, request):
        return render(request, 'sign_in.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home:homepage'))
        else:
            return render(request, 'sign_in.html', {'information_invalid': True})


class sign_up(View):
    def get(self, request):
        return render(request, 'sign_up.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordagain = request.POST.get('passwordagain')
        if len(email) == 0 or len(username) == 0 or len(password) == 0 or len(passwordagain) == 0:
            return render(request, 'sign_up.html', {'username_null': True})
        if not '@' in email:
            return render(request, 'sign_up.html', {'email_invalid': True})
        if password != passwordagain:
            return render(request, 'sign_up.html', {'username': username, 'email': email, 'password_again_error': True})
        try:
            user = User.objects.create_user(username, email, password)
        except ValueError:
            return render(request, 'sign_up.html', {'username_null': True})
        except IntegrityError:
            return render(request, 'sign_up.html', {'username_already_exist': True})
        # After register user member successfully
        Customer.objects.create(username=username, user=user, emailAddress=email)
        return redirect(reverse('home:homepage'))


def email_verification(request):
    return render(request, 'email_verification.html')


def reset_password(request):
    return render(request, 'reset_password.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))