# Generated by Django 5.0.dev20230201122643 on 2023-03-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_account_cluesunlocked_account_gamecompleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='distanceTraveled',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='finalLat',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='finalLng',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='startingLat',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='startingLng',
            field=models.CharField(default='', max_length=100),
        ),
    ]
