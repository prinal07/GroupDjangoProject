# Generated by Django 4.1.7 on 2023-02-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accomodation',
            old_name='accomodation_Name',
            new_name='accomodationName',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='department_Name',
            new_name='departmentName',
        ),
        migrations.AddField(
            model_name='challenge',
            name='challengeTitle',
            field=models.CharField(default='Challenge Title', max_length=50),
            preserve_default=False,
        ),
    ]
