# Generated by Django 5.0.dev20230201122643 on 2023-03-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0018_challenge_delete_challenege_bin_challenge'),
        ('users', '0006_alter_account_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='challenges',
            field=models.ManyToManyField(related_name='accounts', to='game.challenge'),
        ),
    ]
