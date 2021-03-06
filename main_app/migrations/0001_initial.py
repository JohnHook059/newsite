# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 15:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=1000000)),
                ('time', models.DateTimeField(default=datetime.datetime(2016, 10, 27, 15, 38, 19, 517785, tzinfo=utc))),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
