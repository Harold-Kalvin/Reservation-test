# Generated by Django 2.2.2 on 2019-06-26 06:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='capacity',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='The minimum value is 1.')], verbose_name='Capacity'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='localization',
            field=models.CharField(max_length=256, verbose_name='Localization'),
        ),
    ]
