# Generated by Django 4.2.3 on 2023-10-11 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=30, verbose_name='full_name'),
        ),
    ]