# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-06 14:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20180506_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_detail',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 6, 20, 23, 51, 596982)),
        ),
        migrations.AlterField(
            model_name='milk_rate',
            name='up_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 6, 20, 23, 51, 596982)),
        ),
    ]