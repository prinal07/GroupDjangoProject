# Generated by Django 5.0.dev20230201122643 on 2023-03-23 01:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_account_last_bin_scanned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_bin_scanned',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 1, 40, 49, 675456)),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_green_area_accessed',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 1, 40, 49, 675456)),
        ),
    ]
