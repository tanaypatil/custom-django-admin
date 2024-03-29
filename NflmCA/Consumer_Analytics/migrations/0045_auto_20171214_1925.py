# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-14 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer_Analytics', '0044_instapic_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instaalbum',
            options={'verbose_name': 'Instagram Album', 'verbose_name_plural': 'Instagram Albums'},
        ),
        migrations.AlterModelOptions(
            name='instacomments',
            options={'verbose_name': 'Instagram Comment', 'verbose_name_plural': 'Instagram Comments'},
        ),
        migrations.AlterModelOptions(
            name='instapic',
            options={'verbose_name': 'Instagram Pic', 'verbose_name_plural': 'Instagram Pics'},
        ),
        migrations.RemoveField(
            model_name='instaalbum',
            name='name',
        ),
        migrations.AddField(
            model_name='instaalbum',
            name='insta_id',
            field=models.CharField(help_text='Instagram ID', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instaalbum',
            name='username',
            field=models.CharField(help_text='User Name', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='instaalbum',
            name='user',
            field=models.ForeignKey(blank=True, help_text='Consumer Object. Attach if exists.', null=True, on_delete=django.db.models.deletion.CASCADE, to='Consumer_Analytics.User'),
        ),
    ]
