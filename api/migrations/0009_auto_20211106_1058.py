# Generated by Django 3.2.5 on 2021-11-06 01:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20211106_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='training',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 6, 1, 58, 32, 406186, tzinfo=utc), verbose_name='Date'),
        ),
    ]
