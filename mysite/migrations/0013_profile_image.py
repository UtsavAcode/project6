# Generated by Django 4.2.3 on 2023-09-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_remove_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='image'),
        ),
    ]
