# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_auto_20170824_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='likes',
        ),
    ]
