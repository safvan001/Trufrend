# Generated by Django 4.2.7 on 2023-11-02 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trufrend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=None, max_length=15, unique=True),
        ),
    ]
