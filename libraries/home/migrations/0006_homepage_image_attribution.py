# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 22:18
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_protect_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image_attribution',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
