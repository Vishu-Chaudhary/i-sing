# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0023_auto_20170828_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedetail',
            name='profile_id',
            field=models.PositiveIntegerField(),
        ),
    ]
