# Generated by Django 5.0.dev20230201122643 on 2023-02-24 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_accomodation_user_accommodation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='staffCheck',
            field=models.BooleanField(default=False),
        ),
    ]
