# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-01-04 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salon_Analytics', '0004_salon_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='tag',
            field=models.ManyToManyField(blank=True, to='Salon_Analytics.Tag'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_vendor',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='order',
            name='dispatch_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='review',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_id',
            field=models.CharField(blank=True, max_length=35),
        ),
        migrations.AlterField(
            model_name='salon',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
