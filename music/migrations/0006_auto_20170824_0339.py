# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 22:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='song',
            new_name='songref',
        ),
    ]
