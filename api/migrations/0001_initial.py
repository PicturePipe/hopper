# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.conf import settings
from django.db import migrations, models


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
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('action', models.TextField(verbose_name='Form action')),
                ('enctype', models.TextField(verbose_name='Form enctype', default='multipart/form-data')),
                ('method', models.CharField(max_length=4, verbose_name='Field method', choices=[('GET', 'GET'), ('POST', 'POST')], default='GET')),
                ('help_text', models.TextField(null=True, verbose_name='Help text', blank=True)),
                ('css_classes', models.TextField(verbose_name='Form CSS classes', default='')),
                ('elements', django.contrib.postgres.fields.hstore.HStoreField()),
                ('elements_css_classes', models.TextField(verbose_name='Field CSS classes', default='')),
                ('html', models.TextField(null=True, default=None)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
