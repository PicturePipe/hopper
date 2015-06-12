# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HopperUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
