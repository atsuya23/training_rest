# Generated by Django 3.2.5 on 2021-11-20 06:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 6, 55, 57, 66711, tzinfo=utc), verbose_name='Date'),
        ),
    ]
