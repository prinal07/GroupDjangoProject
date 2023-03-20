# Generated by Django 4.1.7 on 2023-03-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0020_alter_story_culprit'),
        ('users', '0012_challengestatus'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChallengeStatus',
            new_name='ChallengeTracker',
        ),
        migrations.AddField(
            model_name='account',
            name='binCounter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='greenCounter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='walkCounter',
            field=models.IntegerField(default=0),
        ),
    ]
