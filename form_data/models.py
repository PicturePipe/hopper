# encoding: utf-8
from __future__ import unicode_literals

import json

from django.conf import settings
from django_pgjson.fields import JsonField
from django.db import models
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

from .forms import HopperForm
from . import managers


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
    elements = JsonField(default={})
    elements_css_classes = models.TextField(verbose_name='Field CSS classes')
    html = models.TextField(verbose_name='HTML', editable=False)

    objects = managers.FormDataManager.from_queryset(managers.FormDataQuerySet)()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(FormData, self).save(*args, **kwargs)


@receiver(models.signals.post_save, sender=FormData)
def render_form_data_html(sender, instance, created, raw, **kwargs):
    """Renders FormData.html after a new FormData has been created."""
    if not raw:
        # to prevent cyclic imports
        from rest_framework.renderers import JSONRenderer
        from api.serializers import FormDataSerializer
        data = FormDataSerializer(instance).data
        instance.html = HopperForm(
            data=JSONRenderer().render(data)
        ).render_as_form()
