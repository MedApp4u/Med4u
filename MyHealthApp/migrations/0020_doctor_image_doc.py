# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyHealthApp', '0019_procedure'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image_doc',
            field=models.ImageField(null=True, upload_to='doctors'),
        ),
    ]