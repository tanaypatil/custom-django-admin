# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-01-07 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salon_Analytics', '0007_auto_20170107_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(null=True),
        ),
    ]
