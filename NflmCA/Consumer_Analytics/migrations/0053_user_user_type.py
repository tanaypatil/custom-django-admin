# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-12-21 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0052_fbeducation_additional'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Customer', 'Customer'), ('Prospect', 'Prospect')], max_length=9, null=True),
        ),
    ]
