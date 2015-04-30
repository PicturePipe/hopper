# encoding: utf-8
from __future__ import unicode_literals

import json

from django.conf import settings
from django.contrib.postgres.fields import HStoreField
from django.db import models
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible

from .forms import HopperForm


@python_2_unicode_compatible
class FormData(models.Model):
    """Represents an complete Form with meta data and form elements"""
    GET = 'GET'
    POST = 'POST'
    FORM_METHODS = (
        (GET, 'GET'),
        (POST, 'POST')
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author')
    title = models.TextField(verbose_name='Form title')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    action = models.TextField(verbose_name='Form action')
    enctype = models.TextField(verbose_name='Form enctype', default='multipart/form-data')
    method = models.CharField(choices=FORM_METHODS, max_length=4, verbose_name='Field method',
        default=GET)
    help_text = models.TextField(verbose_name='Help text', null=True, blank=True)
    css_classes = models.TextField(verbose_name='Form CSS classes', default='')
    elements = HStoreField()
    elements_css_classes = models.TextField(verbose_name='Field CSS classes', default='')
    html = models.TextField(default=None, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.elements = self.convert_values_to_string(self.elements)
        super(FormData, self).save(*args, **kwargs)

    @classmethod
    def convert_to_dict(cls, elements):
        """Converts flat dict to normal dict
        The current implementation of hstore only allows flat
        dictionaries, all values of nested dicts are strings and have to
        convert to python objects."""
        converted_elements = {}
        if type(elements) != dict:
            converted_elements = json.loads(elements)
        else:
            for key, element in elements.items():
                if type(element) == str:
                    converted_elements[key] = json.loads(element)
                else:
                    converted_elements[key] = elements[key]
        return converted_elements

    @classmethod
    def convert_values_to_string(cls, elements):
        """Converts normal dict to flat dict
        The current implementation of hstore only allows flat
        dictionaries, all values of nested dicts have to convert to
        string."""
        converted_elements = {}
        for key, element in elements.items():
            converted_elements[key] = json.dumps(element)
        return converted_elements


@receiver(models.signals.post_save, sender=FormData)
def render_form_data_html(sender, instance, created, raw, **kwargs):
    """Renders FormData.html after a new FormData has been created."""
    if created and not raw:
        from .serializers import FormDataSerializer
        data = FormDataSerializer(instance).data
        data['elements'] = FormData.convert_to_dict(instance.elements)
        instance.html = HopperForm(data=data).render_as_form()
