# Generated by Django 4.2.7 on 2023-12-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0006_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordata',
            name='Language',
            field=models.ManyToManyField(to='AdminSide.languages'),
        ),
    ]
