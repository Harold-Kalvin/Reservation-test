# Generated by Django 2.2.2 on 2019-06-26 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_reservation_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]