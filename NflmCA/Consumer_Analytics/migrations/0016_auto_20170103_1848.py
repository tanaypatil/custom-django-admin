# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-01-03 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0015_auto_20170103_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallink',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
