# Generated by Django 4.2.7 on 2023-12-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0016_doctordata_is_staff_alter_doctordata_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordata',
            name='Aadhaar',
            field=models.FileField(blank=True, null=True, upload_to='doctor/Aadhaar'),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='Aboutme',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='Certificates',
            field=models.FileField(blank=True, null=True, upload_to='doctor/othercertificate'),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='CurrentAddress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='Degrees',
            field=models.FileField(blank=True, null=True, upload_to='doctor/certificate'),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='Diplomas',
            field=models.FileField(blank=True, null=True, upload_to='doctor/diploma'),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='Education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='Email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='Experience',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='GST',
            field=models.FileField(blank=True, null=True, upload_to='doctor/GST'),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='Gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Trans', 'Trans')], default='Male', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='PAN',
            field=models.FileField(blank=True, null=True, upload_to='doctor/PAN'),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='RCI',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='References',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='callDuration',
            field=models.CharField(default='30 Minutes', max_length=15),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='permanentAddress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='phone',
            field=models.CharField(default='', max_length=18),
        ),
    ]