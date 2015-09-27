# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('school', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=20)),
            ],
        ),
    ]
