# Generated by Django 4.2.7 on 2024-01-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordata',
            name='Aadhaar',
            field=models.FileField(blank=True, default='', upload_to='doctor/Aadhaar'),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='Aboutme',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='Certificates',
            field=models.FileField(blank=True, default='', upload_to='doctor/othercertificate'),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='Degrees',
            field=models.FileField(blank=True, default='', upload_to='doctor/certificate'),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='Diplomas',
            field=models.FileField(blank=True, default='', upload_to='doctor/diploma'),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='Dp',
            field=models.FileField(blank=True, default='', upload_to='doctor/Dp'),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='Education',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='Experience',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='GST',
            field=models.FileField(blank=True, default='', upload_to='doctor/GST'),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='Gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')], default='Male', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='PAN',
            field=models.FileField(blank=True, default='', upload_to='doctor/PAN'),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='RCI',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='doctordata',
            name='References',
            field=models.TextField(blank=True, default=''),
        ),
    ]
