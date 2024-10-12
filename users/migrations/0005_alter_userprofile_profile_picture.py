# Generated by Django 4.2.16 on 2024-10-12 12:24

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_gallery_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
