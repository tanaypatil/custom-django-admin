# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-01-01 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0011_auto_20170102_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Consumer_Analytics.User'),
            preserve_default=False,
        ),
    ]
