from django.contrib import admin
from .models import MemberCard, Customer


class MemberCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'servicePlan', 'numOfFault')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastName', 'firstName', 'username', 'emailAddress')
    fields = ('lastName', 'firstName', 'username', 'dateOfBirth', 'emailAddress', 'address', 'identificationCard',
              'phoneNumber', 'memberCard')
    search_fields = ('id', 'lastName', 'firstName', 'username', 'emailAddress')


admin.site.register(MemberCard, MemberCardAdmin)
admin.site.register(Customer, CustomerAdmin)

