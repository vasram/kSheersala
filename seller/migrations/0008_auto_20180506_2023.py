# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-06 14:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_auto_20180506_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_transactions',
            name='transaction_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 6, 20, 23, 33, 907021)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 6, 20, 23, 33, 907021)),
        ),
    ]
