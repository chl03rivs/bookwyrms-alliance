# Generated by Django 4.2.16 on 2024-10-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='temporary_field',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
