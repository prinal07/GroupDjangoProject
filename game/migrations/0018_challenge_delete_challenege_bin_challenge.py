# Generated by Django 5.0.dev20230201122643 on 2023-03-10 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0017_challenege'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challengeId', models.IntegerField(default=1)),
                ('challengeDesc', models.TextField(default='', max_length=400)),
                ('challengeType', models.TextField(choices=[('Bin', 'Bin'), ('GreenAreas', 'GreenAreas'), ('Walking', 'Walking')], default='')),
            ],
        ),
        migrations.DeleteModel(
            name='Challenege',
        ),
        migrations.AddField(
            model_name='bin',
            name='challenge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.challenge'),
        ),
    ]