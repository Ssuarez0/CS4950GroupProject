# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0005_auto_20170509_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
