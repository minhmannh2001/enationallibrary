from django.contrib import admin
from .models import Book, Magazine, New, Collection


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'beingBorrowedQuantity')
    search_fields = ('title',)


class MagazineAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class NewAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Magazine, MagazineAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Collection, CollectionAdmin)