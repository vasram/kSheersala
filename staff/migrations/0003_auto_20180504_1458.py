# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-04 09:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20180501_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_detail',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 14, 58, 27, 86110)),
        ),
        migrations.AlterField(
            model_name='milk_rate',
            name='up_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 14, 58, 27, 86110)),
        ),
    ]
