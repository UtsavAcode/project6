# Generated by Django 4.2.3 on 2023-10-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0022_alter_signup_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254,default='default@example.com', verbose_name='email'),
        ),
    ]
