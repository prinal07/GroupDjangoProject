# Generated by Django 5.0.dev20230201122643 on 2023-03-09 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_alter_story_sprite_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='sprite_2',
            field=models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[0-9]+$')]),
        ),
        migrations.AlterField(
            model_name='story',
            name='sprite_3',
            field=models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[0-9]+$')]),
        ),
        migrations.AlterField(
            model_name='story',
            name='sprite_4',
            field=models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[0-9]+$')]),
        ),
        migrations.AlterField(
            model_name='story',
            name='sprite_5',
            field=models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[0-9]+$')]),
        ),
    ]