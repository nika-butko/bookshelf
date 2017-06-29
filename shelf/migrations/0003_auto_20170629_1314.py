# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20170303_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf',
            name='action',
            field=models.CharField(choices=[('have', 'Have'), ('read', 'Read'), ('want-to-read', 'Want to read'), ('like', 'Like'), ('currently-reading', 'Currently reading')], max_length=200),
        ),
    ]
