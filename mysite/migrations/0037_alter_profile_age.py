# Generated by Django 4.2.3 on 2023-11-07 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0036_profile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=18, verbose_name='age'),
        ),
    ]
