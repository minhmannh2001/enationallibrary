import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'firstName', 'lastName', 'status')

    def changelist_view(self, request, extra_context=None):
        chart_data = (
            Contact.objects.values('status').annotate(cnt=Count('id'))
        )
        json_data = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": json_data}
        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Contact, ContactAdmin)
