# Generated by Django 5.0.7 on 2024-08-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0002_reja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(upload_to='meida'),
        ),
    ]
