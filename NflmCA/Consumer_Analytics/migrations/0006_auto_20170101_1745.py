# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-01-01 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0005_auto_20170101_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone1',
            field=models.CharField(max_length=13),
        ),
    ]
