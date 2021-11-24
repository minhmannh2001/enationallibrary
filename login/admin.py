from django.contrib import admin
from .models import Author, Publisher


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)