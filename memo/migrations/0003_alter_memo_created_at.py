# Generated by Django 3.2.5 on 2021-11-20 06:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0002_alter_memo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 6, 45, 26, 999093, tzinfo=utc)),
        ),
    ]
