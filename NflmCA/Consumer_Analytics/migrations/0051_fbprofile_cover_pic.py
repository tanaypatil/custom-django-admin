# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-12-18 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0050_auto_20171218_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbprofile',
            name='cover_pic',
            field=models.ImageField(null=True, upload_to='fb/', verbose_name='Cover Picture'),
        ),
    ]
