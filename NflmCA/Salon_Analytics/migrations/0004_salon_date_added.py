# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-01-03 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salon_Analytics', '0003_salon_salon_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]