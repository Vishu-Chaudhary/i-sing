# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-25 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='likes',
            field=models.IntegerField(),
        ),
    ]