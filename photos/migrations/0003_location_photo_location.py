# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-22 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='photo_location',
            field=models.CharField(default='nai', max_length=50),
            preserve_default=False,
        ),
    ]
