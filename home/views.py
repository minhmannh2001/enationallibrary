from django.shortcuts import render
from django.http import HttpResponse
from category.models import Magazine
# Create your views here.

def home(request):
    magazine = Magazine.objects.first()
    print(magazine)
    return render(request, 'layout.html', {
        'magazine': magazine,
    })