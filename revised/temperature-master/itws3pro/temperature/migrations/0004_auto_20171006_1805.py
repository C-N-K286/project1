# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0003_auto_20170913_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='soil_mois',
            field=models.CharField(default=60, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temperature',
            name='wat_lvl',
            field=models.CharField(default=90, max_length=250),
            preserve_default=False,
        ),
    ]
