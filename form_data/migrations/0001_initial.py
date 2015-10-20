# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_pgjson.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name='Form title')),
                ('form_id', models.CharField(blank=True, verbose_name='Form CSS selector', max_length=255)),
                ('date_created', models.DateTimeField(editable=False, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(editable=False, verbose_name='Date updated')),
                ('action', models.TextField(verbose_name='Form action')),
                ('enctype', models.TextField(verbose_name='Form enctype', default='multipart/form-data')),
                ('method', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST')], verbose_name='Form method', max_length=4, default='POST')),
                ('help_text', models.TextField(blank=True, null=True, verbose_name='Help text')),
                ('css_classes', models.TextField(verbose_name='Form CSS classes')),
                ('elements', django_pgjson.fields.JsonField(default={})),
                ('elements_css_classes', models.TextField(verbose_name='Field CSS classes')),
                ('html', models.TextField(editable=False, verbose_name='HTML')),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
