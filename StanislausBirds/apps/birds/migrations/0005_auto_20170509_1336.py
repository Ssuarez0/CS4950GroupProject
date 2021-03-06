# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 20:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0004_auto_20170509_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bird',
            options={'ordering': ('name',)},
        ),
        migrations.RenameField(
            model_name='bird',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='bird',
            old_name='Diet',
            new_name='diet',
        ),
        migrations.RenameField(
            model_name='bird',
            old_name='Habitat',
            new_name='habitat',
        ),
        migrations.RenameField(
            model_name='bird',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='bird',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='bird',
            old_name='Sleep',
            new_name='sleep',
        ),
        migrations.RenameField(
            model_name='bird',
            old_name='Slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='bird',
            old_name='Sound',
            new_name='sound',
        ),
        migrations.RenameField(
            model_name='bird',
            old_name='Species',
            new_name='species',
        ),
    ]
