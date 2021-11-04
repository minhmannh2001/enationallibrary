from django.shortcuts import render
from django.http import HttpResponse
from category.models import Magazine
# Create your views here.

def home(request):
    magazine = Magazine.objects.first()
    print(magazine.image.url)
    print(magazine.pdfFile.url)
    return render(request, 'layout.html', {
        'magazine': magazine,
    })