# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150430_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='date_created',
            field=models.DateTimeField(verbose_name='Date created', editable=False),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='date_updated',
            field=models.DateTimeField(verbose_name='Date updated', editable=False),
        ),
    ]
