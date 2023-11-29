from django.db import models
from django.contrib.auth.models import User

CHOICES = (
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Malayalam','Malayalam'),
        ('Tamil','Tamil'),
    )

class Specialty(models.Model):
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.specialization


class DoctorDetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    DOB=models.DateField()
    CurrentAddress=models.TextField()
    permanentAddress=models.TextField()
    phone= models.CharField(max_length=18)
    Degrees=models.FileField(upload_to='doctor/certificate')
    Diplomas=models.FileField(upload_to='doctor/diploma')
    References=models.TextField()
    Certificates=models.FileField(upload_to='doctor/othercertificate')
    RCI=models.TextField()
    PAN=models.FileField(upload_to='doctor/PAN')
    Aadhaar=models.FileField(upload_to='doctor/Aadhaar')
    GST=models.FileField(upload_to='doctor/GST')
    specialties = models.ManyToManyField(Specialty)
    Aboutme=models.TextField()
    Education=models.TextField()
    Experience=models.CharField(max_length=15)
    language=models.CharField(max_length=100,choices=CHOICES)
    callDuration=models.CharField(max_length=15,default='30 Minutes')
class Upload(models.Model):
    sample=models.FileField(upload_to='doctor/sample')
# Create your models here.
