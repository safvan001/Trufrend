from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from os.path import basename
from AdminSide.models import DoctorData

CHOICES = (
        ('Anxiety', 'Anxiety'),
        ('Motivation', 'Motivation'),
        ('Confidence', 'Confidence'),
        ('Sleep', 'Sleep'),
        ('Depression', 'Depression'),
        ('Work Stress', 'Work Stress'),
        ('Relationships', 'Relationships'),
        ('Exam stress', 'Exam stress'),
        ('Pregnancy', 'Pregnancy'),
        ('Loss', 'Loss'),
        ('LGBTQ+', 'LGBTQ+'),
        ('Low Energy', 'Low Energy'),
        ('Self Esteem', 'Self Esteem'),
        ('Loneliness', 'Loneliness'),
        ('Trauma', 'Trauma'),
        ('Health issues', 'Health issues'),
    )

class Challenge(models.Model):
    challenges = models.CharField(max_length=100,choices=CHOICES)
    # challenges=models.CharField(max_length=100)
    def __str__(self):
        return self.challenges
class VideoPack(models.Model):
    video_file = models.FileField(upload_to='videos/',default=1)
    subtitle=models.CharField(max_length=200,default=' ')
    description = models.TextField(default='')
    videolen=models.CharField(max_length=100,default='10')
    image=models.ImageField(upload_to='img/videobanner', null=True, blank=True)

    def __str__(self):
        return basename(str(self.video_file))
    # Add other fields if necessary

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_files = models.ManyToManyField(VideoPack)
    posterimage=models.ImageField(upload_to='img/Posterimage', null=True, blank=True)
    # Add other fields if necessary
    def __str__(self):
        return self.title

class Profile(models.Model):
    phone_number = models.CharField(max_length=15,default='')
    dp = models.ImageField(upload_to='img/profile_pictures', null=True, blank=True,default="img/profile_pictures/userimage.png")
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50)
    challenges = models.ManyToManyField(Challenge)
    videoFavour = models.ManyToManyField(Video)
    doctorFavour=models.ManyToManyField(DoctorData)

    def __str__(self):
        return self.phone_number

class Favorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class ContactUs(models.Model):
    phone_no=models.CharField(max_length=15)
    firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    email= models.CharField(max_length=254)
    subject=models.TextField()
    description=models.TextField()
    def __str__(self):
        return self.firstname


# class Stories(models.Model):
#     story_file = models.FileField(upload_to='stories/')
#
#     # Other fields for your model, if any
#
#     def __str__(self):
#         return str(self.story_file)









