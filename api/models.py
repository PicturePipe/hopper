# encoding: utf-8
from __future__ import unicode_literals

from collections import OrderedDict
import json

from django.conf import settings
from django.contrib.postgres.fields import HStoreField
from django.db import models
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

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
    form_id = models.CharField(verbose_name='Form CSS selector', max_length=255, blank=True)
    date_created = models.DateTimeField(verbose_name='Date created', editable=False)
    date_updated = models.DateTimeField(verbose_name='Date updated', editable=False)
    action = models.TextField(verbose_name='Form action')
    enctype = models.TextField(verbose_name='Form enctype', default='multipart/form-data')
    method = models.CharField(verbose_name='Form method', choices=FORM_METHODS, max_length=4,
        default=POST)
    help_text = models.TextField(verbose_name='Help text', null=True, blank=True)
    css_classes = models.TextField(verbose_name='Form CSS classes')
    elements = HStoreField()
    elements_css_classes = models.TextField(verbose_name='Field CSS classes')
    html = models.TextField(verbose_name='HTML', editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.elements = self.convert_values_to_string(self.elements)
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(FormData, self).save(*args, **kwargs)

    @classmethod
    def convert_to_dict(cls, elements):
        """Converts flat dict to normal dict
        The current implementation of hstore only allows flat
        dictionaries, all values of nested dicts are strings and have to
        convert to python objects."""
        converted_elements = {}
        if elements:
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
        if elements:
            for key, element in elements.items():
                converted_elements[key] = json.dumps(element)
        return converted_elements

    @classmethod
    def order_by_weight(cls, elements):
        ordered_elements = elements.copy()
        for name, element in elements.items():
            if element.get('type') == 'fieldset':
                ordered_elements[name]['elements'] = cls.order_by_weight(element['elements'])
        return OrderedDict(
            sorted(ordered_elements.items(), key=lambda element: element[1].get('weight', 10000))
        )


@receiver(models.signals.post_save, sender=FormData)
def render_form_data_html(sender, instance, created, raw, **kwargs):
    """Renders FormData.html after a new FormData has been created."""
    if not raw:
        # to prevent cyclic imports
        from rest_framework.renderers import JSONRenderer
        from .serializers import FormDataSerializer
        data = FormDataSerializer(instance).data
        instance.html = HopperForm(
            data=JSONRenderer().render(data)
        ).render_as_form().replace('\n', '').replace('\t', '')
