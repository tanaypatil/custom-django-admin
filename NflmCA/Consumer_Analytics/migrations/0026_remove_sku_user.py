# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-01-07 09:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0025_sku_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sku',
            name='user',
        ),
    ]