# Generated by Django 4.2.1 on 2023-06-27 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_is_autheniceated_alter_user_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_autheniceated',
            new_name='is_authenticated',
        ),
    ]