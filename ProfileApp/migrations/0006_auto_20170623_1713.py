# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0005_auto_20170623_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=b'Images/profile'),
        ),
    ]