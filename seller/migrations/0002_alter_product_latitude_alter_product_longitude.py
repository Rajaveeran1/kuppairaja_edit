# Generated by Django 4.1 on 2023-03-04 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='latitude',
            field=models.FloatField(default=11.749710927476007),
        ),
        migrations.AlterField(
            model_name='product',
            name='longitude',
            field=models.FloatField(default=79.76045317140348),
        ),
    ]
