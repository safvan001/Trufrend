from django.db import models
from django.contrib.auth.models import User



class Specialty(models.Model):
    specialization = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.specialization
class Language(models.Model):
    Languages=models.CharField(max_length=100,default='')
    def __str__(self):
        return self.Languages


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
    Aboutme=models.TextField()
    Education=models.TextField()
    Experience=models.CharField(max_length=100)
    callDuration=models.CharField(max_length=15,default='30 Minutes')
class Upload(models.Model):
    sample=models.FileField(upload_to='doctor/sample')
# Create your models here.
