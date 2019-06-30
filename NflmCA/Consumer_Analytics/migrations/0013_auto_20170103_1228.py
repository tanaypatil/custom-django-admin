# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-01-03 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0012_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age_range',
            field=models.CharField(blank=True, choices=[('10-15', '10-15'), ('15-18', '15-18'), ('18-20', '18-20'), ('20-25', '20-25'), ('25-30', '25-30'), ('30-35', '30-35'), ('35-40', '35-40'), ('40-45', '40-45'), ('45-50', '45-50'), ('50-55', '50-55')], default='0', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], default='m', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='income_level',
            field=models.CharField(blank=True, choices=[('affluent', 'affluent'), ('UpperMiddle', 'UpperMiddle'), ('LowerMiddle', 'LowerMiddle')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('married', 'married'), ('unmarried', 'unmarried'), ('divorced', ' divorced')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='occupation',
            field=models.CharField(blank=True, choices=[('student', 'student'), ('Working', 'Working'), ('Housewife', 'Housewife'), ('Other', 'Other')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='occupation_details',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='places_lived',
            field=models.ManyToManyField(blank=True, null=True, to='Consumer_Analytics.City'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
    ]