# Generated by Django 4.1.7 on 2023-03-28 10:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfiguration_data', '0002_rename_titles_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='priority',
            field=models.IntegerField(blank=True, default='', unique=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
