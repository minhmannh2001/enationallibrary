from django.shortcuts import render

# Create your views here.


def sign_in(request):
    return render(request, 'sign_in.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def email_verification(request):
    return render(request, 'email_verification.html')


def reset_password(request):
    return render(request, 'reset_password.html')