# Generated by Django 4.2.7 on 2023-12-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0003_remove_doctordata_callduration'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordata',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]