# Generated by Django 4.2.7 on 2023-12-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0005_stories_media_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]