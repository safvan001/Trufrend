# Generated by Django 4.2.7 on 2023-12-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0003_alter_doctordata_gender'),
        ('Trufrend', '0005_alter_profile_dp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='doctorFavour',
            field=models.ManyToManyField(to='AdminSide.doctordata'),
        ),
    ]
