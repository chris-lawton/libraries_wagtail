# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Closure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(help_text='e.g. Meyer Fall 2017', max_length=200)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
            ],
        ),
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name_plural': 'libraries'},
        ),
        migrations.AlterModelOptions(
            name='openhours',
            options={'verbose_name_plural': 'open hours'},
        ),
        migrations.AddField(
            model_name='closure',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='hours.Library'),
        ),
    ]
