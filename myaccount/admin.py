from django.contrib import admin
from .models import MemberCard, User


class MemberCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'servicePlan', 'numOfFault')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastName', 'firstName', 'username', 'emailAddress')
    search_fields = ('id', 'lastName', 'firstName', 'username', 'emailAddress')


admin.site.register(MemberCard, MemberCardAdmin)
admin.site.register(User, UserAdmin)

