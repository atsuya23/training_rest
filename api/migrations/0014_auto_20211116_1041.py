# Generated by Django 3.2.5 on 2021-11-16 01:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20211116_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 11, 16, 1, 41, 9, 364530, tzinfo=utc), null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='training',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 16, 1, 41, 9, 364530, tzinfo=utc), verbose_name='Date'),
        ),
    ]
