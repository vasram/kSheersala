# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-30 21:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20180501_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_transactions',
            name='transaction_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 1, 2, 48, 28, 529060)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 1, 2, 48, 28, 529060)),
        ),
    ]