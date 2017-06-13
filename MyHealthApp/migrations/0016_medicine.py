# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyHealthApp', '0015_auto_20170609_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dossage_amt', models.FloatField()),
                ('method', models.CharField(choices=[('s', 'tablet'), ('p', 'powder'), ('ml', 'liquid ml')], default='s', max_length=2)),
                ('frequency', models.IntegerField()),
                ('date', models.DateField()),
                ('notes', models.TextField()),
                ('doctors', models.ManyToManyField(to='MyHealthApp.Doctor')),
            ],
        ),
    ]