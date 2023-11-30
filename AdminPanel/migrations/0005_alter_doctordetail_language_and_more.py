# Generated by Django 4.2.7 on 2023-11-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0004_alter_doctordetail_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetail',
            name='language',
            field=models.ManyToManyField(to='AdminPanel.language'),
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='specialties',
            field=models.ManyToManyField(to='AdminPanel.specialty'),
        ),
    ]
