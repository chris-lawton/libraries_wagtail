# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0006_hourspage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openhours',
            name='fri',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='openhours',
            name='mon',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='openhours',
            name='sat',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='openhours',
            name='sun',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='openhours',
            name='thu',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='openhours',
            name='tue',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='openhours',
            name='wed',
            field=models.CharField(max_length=150),
        ),
    ]
