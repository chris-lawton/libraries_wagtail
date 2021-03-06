# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0025_row_summary_richtext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuspage',
            name='main_image',
            field=models.ForeignKey(blank=True, help_text='Displays 404px wide on page with a preserved aspect ratio. If this page shows in one of the Services/Collections/About rows, a thumbnail close to 230x115px is generated.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='externallink',
            name='main_image',
            field=models.ForeignKey(blank=True, help_text='If this page shows in one of the Services/Collections/About rows, a thumbnail close to 230x115px is generated.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='main_image',
            field=models.ForeignKey(blank=True, help_text='Displays 404px wide on page with a preserved aspect ratio. If this page shows in one of the Services/Collections/About rows, a thumbnail close to 230x115px is generated.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='specialcollection',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Close to a 2.25-by-1 aspect ratio is bst, image is sized to 910x400px at its largest.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
    ]
