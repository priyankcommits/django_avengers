# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('power', models.IntegerField(default=0)),
                ('icon', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('powers', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('is_god', models.BooleanField(default=False)),
            ],
        ),
    ]
