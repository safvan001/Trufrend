# Generated by Django 4.2.7 on 2023-12-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trufrend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dp',
            field=models.ImageField(blank=True, default='C:/Users/User/Downloads/userimage.png', null=True, upload_to='img/profile_pictures'),
        ),
    ]
