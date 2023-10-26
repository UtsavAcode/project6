# Generated by Django 4.2.3 on 2023-10-24 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0018_profile_email_alter_signup_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mysite.signup'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(default='1', max_length=254, verbose_name='email'),
        ),
    ]