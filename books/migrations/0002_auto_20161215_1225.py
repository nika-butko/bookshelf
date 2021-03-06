# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-15 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='teaser',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='pub_date',
            field=models.DateField(blank=True),
        ),
    ]
