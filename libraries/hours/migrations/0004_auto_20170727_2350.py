# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 23:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0003_auto_20170727_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='openhours',
            old_name='satur',
            new_name='sat',
        ),
        migrations.RenameField(
            model_name='openhours',
            old_name='thurs',
            new_name='thu',
        ),
        migrations.RenameField(
            model_name='openhours',
            old_name='tues',
            new_name='tue',
        ),
        migrations.RenameField(
            model_name='openhours',
            old_name='wednes',
            new_name='wed',
        ),
    ]
