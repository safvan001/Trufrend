# Generated by Django 4.2.7 on 2023-12-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0007_remove_doctordata_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordata',
            name='Gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Trans', 'Trans')], default='Male', max_length=100),
        ),
    ]
