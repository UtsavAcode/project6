# Generated by Django 4.2.3 on 2023-10-31 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0026_rename_user_name_signup_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
    ]