from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password, **extra_fields):
#         if not username:
#             raise ValueError('The username field must be set')
#         username = self.model.normalize_username(username)
#         user = self.model(username=username, **extra_fields)
#         user.set_password(default='asmi@233')
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         return self.create_user(username, password, **extra_fields)
#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(null=True,blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     # Profile fields
#     DOB = models.DateField(null=True, blank=True)
#     current_address = models.TextField(null=True,blank=True)
#     permanent_address = models.TextField(null=True,blank=True)
#     phone = models.CharField(max_length=18,null=True,blank=True)
#     degrees = models.FileField(upload_to='doctor/certificate',null=True,blank=True)
#     diplomas = models.FileField(upload_to='doctor/diploma',null=True,blank=True)
#     references = models.TextField(null=True,blank=True)
#     certificates = models.FileField(upload_to='doctor/othercertificate',null=True,blank=True)
#     rci = models.TextField(null=True,blank=True)
#     pan = models.FileField(upload_to='doctor/PAN',null=True,blank=True)
#     aadhaar = models.FileField(upload_to='doctor/Aadhaar',null=True,blank=True)
#     gst = models.FileField(upload_to='doctor/GST',null=True,blank=True)
#     about_me = models.TextField(null=True,blank=True)
#     education = models.TextField(null=True,blank=True)
#     experience = models.CharField(max_length=100,null=True,blank=True)
#     call_duration = models.CharField(max_length=15, default='30 Minutes')
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     def __str__(self):
#         return self.username

class Languages(models.Model):
    languages=models.CharField(max_length=100)
    def __str__(self):
        return self.languages
class Specality(models.Model):
    specialization=models.CharField(max_length=100)
    def __str__(self):
        return self.specialization
class DoctorData(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=128)
    Dp=models.FileField(upload_to='doctor/Dp',null=True,blank=True)
    DOB = models.DateField(null=True,blank=True)
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Trans', 'Trans'),
    )
    Gender=models.CharField(max_length=100,choices=CHOICES,blank=True,default='Male')
    Language=models.ManyToManyField(Languages)
    Specialization=models.ManyToManyField(Specality)
    CurrentAddress = models.TextField(null=True,blank=True)
    permanentAddress = models.TextField(null=True,blank=True)
    name=models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=18)
    Email=models.EmailField(blank=True)
    Degrees = models.FileField(upload_to='doctor/certificate',null=True,blank=True)
    Diplomas = models.FileField(upload_to='doctor/diploma',null=True,blank=True)
    References = models.TextField(null=True,blank=True)
    Certificates = models.FileField(upload_to='doctor/othercertificate',null=True,blank=True)
    RCI = models.TextField(null=True,blank=True)
    PAN = models.FileField(upload_to='doctor/PAN',null=True,blank=True)
    Aadhaar = models.FileField(upload_to='doctor/Aadhaar',null=True,blank=True)
    GST = models.FileField(upload_to='doctor/GST',null=True,blank=True)
    Aboutme = models.TextField(null=True,blank=True)
    Education = models.TextField(null=True,blank=True)
    Experience = models.CharField(max_length=100,null=True,blank=True)
    callDuration = models.CharField(max_length=15, default='30 Minutes')

    def save(self, *args, **kwargs):
        # Handle password hashing before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    # def check_password(self, raw_password):
    #     return check_password(raw_password, self.password)

    def __str__(self):
        return self.phone


# Create your models here.
