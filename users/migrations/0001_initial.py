# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HopperUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('username', models.CharField(max_length=200)),
                ('is_master', models.BooleanField(default=False)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='hopperuser',
            unique_together=set([('username', 'site')]),
        ),
    ]
