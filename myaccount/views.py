from django.shortcuts import render
from django.views import View


class MyProfile(View):
    def get(self, request):
        is_login = False
        is_staff = False
        if not request.user.is_anonymous:
            is_login = True
        if request.user.is_staff:
            is_staff = True
        return render(request, 'my_profile.html', {
            'is_login': is_login,
            'is_staff': is_staff,
            'user': request.user,
        })


class MyCart(View):
    def get(self, request):
        return render(request, 'my_profile.html')


class MyBorrowedBooks(View):
    def get(self, request):
        return render(request, 'my_profile.html')


class MyPlan(View):
    def get(self, request):
        return render(request, 'my_profile.html')

