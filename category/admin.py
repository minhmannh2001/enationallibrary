from django.contrib import admin
from .models import Book, Magazine, News, Collection


# Register your models here.
admin.site.register(Book)
admin.site.register(Magazine)
admin.site.register(News)
admin.site.register(Collection)