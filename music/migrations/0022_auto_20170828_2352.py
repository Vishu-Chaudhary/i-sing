# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 18:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0021_auto_20170828_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedetail',
            name='profile_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
