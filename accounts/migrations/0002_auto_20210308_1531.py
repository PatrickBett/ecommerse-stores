# Generated by Django 3.1.5 on 2021-03-08 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Firstname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Lastname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Middlename',
            new_name='middlename',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Password1',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Password2',
            new_name='password2',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='PhoneNo',
            new_name='phoneno',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Username',
            new_name='username',
        ),
    ]
