# Generated by Django 4.2.3 on 2023-09-29 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_remove_profile_hobbies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='images/', verbose_name='picture'),
        ),
    ]
