# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-01-03 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0018_auto_20170103_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(help_text='Date Of Birth', null=True),
        ),
    ]
