from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('eventName', 'startDate', 'endDate')
    search_fields = ('eventName',)


# Register your models here.
admin.site.register(Event, EventAdmin)
