# Generated by Django 5.0.dev20230201122643 on 2023-03-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_riddle_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='bin_or_area_id',
            field=models.IntegerField(default=1),
        ),
    ]
