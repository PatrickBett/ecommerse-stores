# Generated by Django 3.1.5 on 2021-03-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
