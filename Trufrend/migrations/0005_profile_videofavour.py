# Generated by Django 4.2.7 on 2023-12-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trufrend', '0004_delete_videofavourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='videoFavour',
            field=models.ManyToManyField(to='Trufrend.video'),
        ),
    ]
