# Generated by Django 4.2.7 on 2023-11-13 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trufrend', '0015_alter_challenge_challenges'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='challenges',
        ),
        migrations.AddField(
            model_name='profile',
            name='challenges',
            field=models.ManyToManyField(to='Trufrend.challenge'),
        ),
    ]