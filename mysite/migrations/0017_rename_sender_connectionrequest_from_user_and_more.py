# Generated by Django 4.2.3 on 2023-10-17 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_connectionrequest'),
    ]


    operations = [
        migrations.RenameField(
            model_name='connectionrequest',
            old_name='sender',
            new_name='from_user',
        ),
        migrations.RenameField(
            model_name='connectionrequest',
            old_name='receiver',
            new_name='to_user',
        ),
        migrations.RemoveField(
            model_name='connectionrequest',
            name='timestamp',
        ),
    ]
