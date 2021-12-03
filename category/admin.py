from django.contrib import admin
from django.utils.html import format_html
from .models import Book, Magazine, New, Collection


class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'type', 'author', 'publisher', 'language', 'description', 'summary', 'image', 'show_image',
              'quantity', 'beingBorrowedQuantity', 'genre', 'rating')
    readonly_fields = ('show_image',)
    list_display = ('title', 'show_image2', 'quantity', 'beingBorrowedQuantity')
    search_fields = ('title',)
    list_per_page = 6

    def show_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" height="200px"/>')
    show_image.short_description = "Ảnh đã chọn"

    def show_image2(self, obj):
        return format_html(f'<img src="{obj.image.url}" height="120px"/>')
    show_image2.short_description = "Ảnh bìa"


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