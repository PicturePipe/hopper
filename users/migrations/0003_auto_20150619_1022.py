# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('users', '0002_auto_20150618_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hopperuser',
            options={'verbose_name_plural': 'users', 'verbose_name': 'user'},
        ),
        migrations.AddField(
            model_name='hopperuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='hopperuser',
            name='first_name',
            field=models.CharField(max_length=30, blank=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='hopperuser',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', related_name='user_set', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', blank=True),
        ),
        migrations.AddField(
            model_name='hopperuser',
            name='is_superuser',
            field=models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='hopperuser',
            name='last_name',
            field=models.CharField(max_length=30, blank=True, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='hopperuser',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', related_name='user_set', verbose_name='user permissions', help_text='Specific permissions for this user.', related_query_name='user', blank=True),
        ),
        migrations.AlterField(
            model_name='hopperuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='hopperuser',
            unique_together=set([('email', 'site')]),
        ),
        migrations.RemoveField(
            model_name='hopperuser',
            name='username',
        ),
    ]
