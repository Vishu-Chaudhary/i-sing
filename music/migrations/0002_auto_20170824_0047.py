# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='likes',
        ),
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to='music.Profile'),
        ),
    ]
