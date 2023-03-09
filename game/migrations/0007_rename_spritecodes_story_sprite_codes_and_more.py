# Generated by Django 5.0.dev20230201122643 on 2023-03-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_remove_story_sprite_codes_remove_story_story_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='spriteCodes',
            new_name='sprite_codes',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='storyNumber',
            new_name='story_number',
        ),
        migrations.AlterField(
            model_name='story',
            name='clue1',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='story',
            name='clue10',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='story',
            name='clue2',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='story',
            name='clue3',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='story',
            name='clue4',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='story',
            name='clue5',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='story',
            name='clue6',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='story',
            name='clue7',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='story',
            name='clue8',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='story',
            name='clue9',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='suspect',
            name='brief',
            field=models.TextField(default='', max_length=150),
        ),
    ]
