# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-07 04:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0011_auto_20180507_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_transactions',
            name='transaction_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 7, 9, 37, 31, 794148)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 7, 9, 37, 31, 794148)),
        ),
    ]
