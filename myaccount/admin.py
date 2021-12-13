from django.contrib import admin
from .models import MemberCard, Customer, OrderedBooks


class MemberCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'servicePlan', 'numOfFault')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastName', 'firstName', 'username', 'emailAddress')
    fields = ('lastName', 'firstName', 'username', 'dateOfBirth', 'emailAddress', 'address', 'identificationCard',
              'phoneNumber', 'memberCard')
    search_fields = ('id', 'lastName', 'firstName', 'username', 'emailAddress')


class OrderedBooksAdmin(admin.ModelAdmin):
    list_display = ('book', 'customer', 'ordered_date', 'expired_date', 'status')
    readonly_fields = ('ordered_date',)
    fields = ('book', 'customer', 'expired_date', 'status')
    search_fields = ('book', 'customer')


admin.site.register(MemberCard, MemberCardAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(OrderedBooks, OrderedBooksAdmin)

