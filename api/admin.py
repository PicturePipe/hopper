# encoding: utf-8
from django.contrib import admin

from .models import FormData


class FormDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'method', 'action', 'enctype',
        'css_classes', 'elements_css_classes', 'help_text', 'date_created', 'date_updated')
    list_filter = ('method', )
    search_fields = ('title', )

admin.site.register(FormData, FormDataAdmin)
