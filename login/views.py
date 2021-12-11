from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


def sign_in(request):
    return render(request, 'sign_in.html')


class sign_up(View):
    def get(self, request):
        return render(request, 'sign_up.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordagain = request.POST.get('passwordagain')
        if password != passwordagain:
            return render(request, 'sign_up.html', {'username': username, 'email': email, 'password_again_error': True})
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(request, 'sign_up.html', {'username_already_exist': True})
        return redirect(reverse('home:homepage'))


def email_verification(request):
    return render(request, 'email_verification.html')


def reset_password(request):
    return render(request, 'reset_password.html')