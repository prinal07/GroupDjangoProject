# Generated by Django 5.0.dev20230201122643 on 2023-03-13 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0019_alter_challenge_challengetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='culprit',
            field=models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[0-4]$')]),
        ),
    ]
