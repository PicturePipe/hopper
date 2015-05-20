# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='form_id',
            field=models.CharField(max_length=255, verbose_name='Form CSS selector', blank=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='css_classes',
            field=models.TextField(verbose_name='Form CSS classes'),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='elements_css_classes',
            field=models.TextField(verbose_name='Field CSS classes'),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='html',
            field=models.TextField(verbose_name='HTML', editable=False),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='method',
            field=models.CharField(max_length=4, default='POST', verbose_name='Form method', choices=[('GET', 'GET'), ('POST', 'POST')]),
        ),
    ]
