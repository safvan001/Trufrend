# Generated by Django 4.2.7 on 2023-12-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0015_remove_doctordata_aadhaar_remove_doctordata_aboutme_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordata',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
