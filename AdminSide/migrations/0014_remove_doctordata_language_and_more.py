# Generated by Django 4.2.7 on 2023-12-05 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0013_alter_languages_languages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctordata',
            name='Language',
        ),
        migrations.RemoveField(
            model_name='doctordata',
            name='Specialization',
        ),
        migrations.DeleteModel(
            name='Languages',
        ),
        migrations.DeleteModel(
            name='Specality',
        ),
    ]
