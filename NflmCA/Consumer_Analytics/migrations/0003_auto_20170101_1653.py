# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-01-01 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0002_auto_20170101_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
    ]
