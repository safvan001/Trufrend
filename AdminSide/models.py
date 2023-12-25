from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# from Trufrend.models import VideoPack
from django.db import models
from django.utils import timezone

# class DoctorDataManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The username field must be set')
#
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         return self.create_user(username, password, **extra_fields)






# class DoctorDataManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The username must be set')
#
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password=None, **extra_fields):
#         # Set any superuser-specific fields here
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         return self.create_user(username, password, **extra_fields)
#
# class DoctorData(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=100, unique=True)
#     Dp=models.FileField(upload_to='doctor/Dp',null=True,blank=True)
#     DOB = models.DateField(null=True,blank=True)
#     CHOICES = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ('Trans', 'Trans'),
#     )
#     Gender=models.CharField(max_length=100,choices=CHOICES,null=True,blank=True,default='Male')
#     # Language=models.ManyToManyField(Languages)
#     # Specialization=models.ManyToManyField(Specality)
#     CurrentAddress = models.TextField(null=True,blank=True)
#     permanentAddress = models.TextField(null=True,blank=True)
#     name=models.CharField(max_length=100,blank=True,null=True)
#     phone = models.CharField(max_length=18,default='')
#     Email=models.EmailField(null=True,blank=True)
#     # story = models.ForeignKey(Stories, on_delete=models.SET_NULL, null=True, blank=True)
#     # stories = models.ManyToManyField(Stories, blank=True)
#     Degrees = models.FileField(upload_to='doctor/certificate',null=True,blank=True)
#     Diplomas = models.FileField(upload_to='doctor/diploma',null=True,blank=True)
#     References = models.TextField(null=True,blank=True)
#     Certificates = models.FileField(upload_to='doctor/othercertificate',null=True,blank=True)
#     RCI = models.TextField(null=True,blank=True)
#     PAN = models.FileField(upload_to='doctor/PAN',null=True,blank=True)
#     Aadhaar = models.FileField(upload_to='doctor/Aadhaar',null=True,blank=True)
#     GST = models.FileField(upload_to='doctor/GST',null=True,blank=True)
#     Aboutme = models.TextField(null=True,blank=True)
#     Education = models.TextField(null=True,blank=True)
#     Experience = models.CharField(max_length=100,null=True,blank=True)
#     callDuration = models.CharField(max_length=15, default='30 Minutes')
#     # Add other fields as needed
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     objects = DoctorDataManager()
#
#     USERNAME_FIELD = 'username'
#
#     def __str__(self):
#         return self.username


class Specality(models.Model):
    specialization=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.specialization
class Languages(models.Model):
    languages=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.languages

class Stories(models.Model):
    story_file = models.FileField(upload_to='stories/',blank=True,default='')
    created_at = models.DateTimeField(default=timezone.now,null=True,blank=True)
    media_type=models.TextField(null=True,blank=True)
class DoctorData(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=128)
    Dp=models.FileField(upload_to='doctor/Dp',null=True,blank=True)
    DOB = models.DateField(null=True,blank=True)
    is_online = models.BooleanField(default=False)
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('others', 'others'),
    )
    Gender=models.CharField(max_length=100,choices=CHOICES,null=True,blank=True,default='Male')
    Language=models.ManyToManyField(Languages,blank=True)
    Specialization=models.ManyToManyField(Specality,blank=True)
    CurrentAddress = models.TextField(null=True,blank=True)
    permanentAddress = models.TextField(null=True,blank=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=18)
    Email=models.EmailField(null=True,blank=True)
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
    # callDuration = models.CharField(max_length=15, default='30 Minutes', null=True, blank=True)
    created_at=models.DateTimeField(default=timezone.now,null=True,blank=True)
    from Trufrend.models import Video
    VideoFavour=models.ManyToManyField(Video,blank=True)
    story=models.ManyToManyField(Stories, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     # Handle password hashing before saving
    #     self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

    # def check_password(self, raw_password):
    #     return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
class Remainder(models.Model):
    date=models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.date




# class Stories(models.Model):
#     story_file = models.FileField(upload_to='stories/',null=True,blank=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     doctor = models.ForeignKey(DoctorData, on_delete=models.CASCADE, related_name='stories',default='')
#     media_type=models.TextField(null=True,blank=True)

    # def __str__(self):
    #     return str(self.story_file)
class Quotes(models.Model):
    quotes=models.TextField(null=True,blank=True)
    author=models.CharField(max_length=200)
    def __str__(self):
        return self.author

# Create your models here.
