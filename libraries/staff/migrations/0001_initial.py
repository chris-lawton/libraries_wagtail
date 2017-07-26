# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 03:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        # dependent on categories because we're creating a StaffListPage
        # that's a child of the "About Us" categories.CategoryPage
        ('categories', '0013_aboutus_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffListPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('main_image', models.ForeignKey(help_text='Only used in search results right now', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StaffPageStaffMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(help_text='In form "555.555.5555"', max_length=12)),
                ('position', models.CharField(max_length=150)),
                ('bio', wagtail.wagtailcore.fields.RichTextField(help_text='A single 4-5 sentence paragraph.')),
                ('main_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_members', to='staff.StaffListPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
