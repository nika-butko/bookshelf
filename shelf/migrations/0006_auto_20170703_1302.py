# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0005_auto_20170629_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf',
            name='action',
            field=models.CharField(choices=[('like', 'Like'), ('currently-reading', 'Currently reading'), ('read', 'Read'), ('want-to-read', 'Want to read'), ('have', 'Have')], max_length=200),
        ),
    ]
