# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='hopperuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='hopperuser',
            name='email',
            field=models.EmailField(verbose_name='email address', blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='hopperuser',
            name='is_active',
            field=models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
        ),
        migrations.AddField(
            model_name='hopperuser',
            name='is_staff',
            field=models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.'),
        ),
        migrations.AlterField(
            model_name='hopperuser',
            name='username',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
