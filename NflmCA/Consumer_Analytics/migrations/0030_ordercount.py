# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-03-11 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0029_auto_20170107_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=40)),
                ('order_count', models.IntegerField()),
            ],
        ),
    ]
