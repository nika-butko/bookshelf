# Generated by Django 2.0.7 on 2018-07-19 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20180716_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, to='books.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(blank=True, to='books.Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.ManyToManyField(blank=True, to='books.Series'),
        ),
        migrations.AlterField(
            model_name='book',
            name='translators',
            field=models.ManyToManyField(blank=True, to='books.Translator'),
        ),
    ]
