# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_auto_20160606_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='is_free',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='parking',
            name='status',
            field=models.CharField(choices=[('No car parking', 'No car parking'), ('Service unavailable', 'Service unavailable')], default='No car parking', max_length=255),
            preserve_default=False,
        ),
    ]
