# Generated by Django 4.2.7 on 2023-12-07 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=128)),
                ('Dp', models.FileField(blank=True, null=True, upload_to='doctor/Dp')),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Trans', 'Trans')], default='Male', max_length=100, null=True)),
                ('CurrentAddress', models.TextField(blank=True, null=True)),
                ('permanentAddress', models.TextField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=18)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Degrees', models.FileField(blank=True, null=True, upload_to='doctor/certificate')),
                ('Diplomas', models.FileField(blank=True, null=True, upload_to='doctor/diploma')),
                ('References', models.TextField(blank=True, null=True)),
                ('Certificates', models.FileField(blank=True, null=True, upload_to='doctor/othercertificate')),
                ('RCI', models.TextField(blank=True, null=True)),
                ('PAN', models.FileField(blank=True, null=True, upload_to='doctor/PAN')),
                ('Aadhaar', models.FileField(blank=True, null=True, upload_to='doctor/Aadhaar')),
                ('GST', models.FileField(blank=True, null=True, upload_to='doctor/GST')),
                ('Aboutme', models.TextField(blank=True, null=True)),
                ('Education', models.TextField(blank=True, null=True)),
                ('Experience', models.CharField(blank=True, max_length=100, null=True)),
                ('callDuration', models.CharField(default='30 Minutes', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_file', models.FileField(blank=True, null=True, upload_to='stories/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
