# Generated by Django 5.0.dev20230201122643 on 2023-03-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_remove_story_sprite_codes_story_sprite_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='sprite_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='story',
            name='sprite_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='story',
            name='sprite_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='story',
            name='sprite_4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='story',
            name='sprite_5',
            field=models.IntegerField(default=0),
        ),
    ]