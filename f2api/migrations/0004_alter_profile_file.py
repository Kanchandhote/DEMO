# Generated by Django 4.1.7 on 2023-03-14 12:28

from django.db import migrations, models
import f2api.models


class Migration(migrations.Migration):

    dependencies = [
        ('f2api', '0003_alter_profile_file_alter_profile_folder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='file',
            field=models.ImageField(blank=True, upload_to=f2api.models.Profile.fileName),
        ),
    ]
