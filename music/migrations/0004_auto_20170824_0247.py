# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20170824_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='music.Profile'),
        ),
    ]
