# Generated by Django 4.2.7 on 2023-12-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trufrend', '0012_alter_usercount_user_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercount',
            name='user_count',
            field=models.IntegerField(),
        ),
    ]
