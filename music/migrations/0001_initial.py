# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-25 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('genre', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to=b'')),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=250)),
                ('file', models.FileField(default='', upload_to=b'')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(max_length=100000)),
                ('is_liked', models.BooleanField(default=False)),
            ],
        ),
    ]
