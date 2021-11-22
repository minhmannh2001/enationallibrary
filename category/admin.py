from django.contrib import admin
from .models import Book, Magazine, New, Collection


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'beingBorrowedQuantity')
    search_fields = ('title',)


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Magazine)
admin.site.register(New)
admin.site.register(Collection)