# Generated by Django 4.2.7 on 2023-11-30 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0008_alter_language_languages_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctordetail',
            name='language',
        ),
        migrations.RemoveField(
            model_name='doctordetail',
            name='specialties',
        ),
    ]
