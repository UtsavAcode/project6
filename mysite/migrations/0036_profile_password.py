# Generated by Django 4.2.3 on 2023-11-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0035_signup_registration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default=11, max_length=250, verbose_name='password'),
            preserve_default=False,
        ),
    ]
