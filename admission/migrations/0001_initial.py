# Generated by Django 3.1.5 on 2021-03-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('contacts', models.IntegerField()),
                ('school', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=30)),
                ('studentphoto', models.ImageField(upload_to='static')),
                ('result_slip', models.ImageField(upload_to='static')),
                ('birthcertificate', models.ImageField(upload_to='static')),
            ],
        ),
    ]
