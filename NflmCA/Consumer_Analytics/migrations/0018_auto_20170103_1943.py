# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-01-03 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0017_auto_20170103_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='occupation_details',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_persona',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
