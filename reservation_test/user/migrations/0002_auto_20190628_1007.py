# Generated by Django 2.2.2 on 2019-06-28 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timezone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Timezone'),
        ),
    ]
