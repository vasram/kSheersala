# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-30 22:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_detail',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 1, 3, 57, 3, 683156)),
        ),
        migrations.AlterField(
            model_name='milk_rate',
            name='up_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 1, 3, 57, 3, 683156)),
        ),
    ]
