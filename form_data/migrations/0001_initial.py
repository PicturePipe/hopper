# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.hstore
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Form title')),
                ('form_id', models.CharField(verbose_name='Form CSS selector', blank=True, max_length=255)),
                ('date_created', models.DateTimeField(verbose_name='Date created', editable=False)),
                ('date_updated', models.DateTimeField(verbose_name='Date updated', editable=False)),
                ('action', models.TextField(verbose_name='Form action')),
                ('enctype', models.TextField(verbose_name='Form enctype', default='multipart/form-data')),
                ('method', models.CharField(verbose_name='Form method', default='POST', choices=[('GET', 'GET'), ('POST', 'POST')], max_length=4)),
                ('help_text', models.TextField(verbose_name='Help text', blank=True, null=True)),
                ('css_classes', models.TextField(verbose_name='Form CSS classes')),
                ('elements', django.contrib.postgres.fields.hstore.HStoreField()),
                ('elements_css_classes', models.TextField(verbose_name='Field CSS classes')),
                ('html', models.TextField(verbose_name='HTML', editable=False)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
