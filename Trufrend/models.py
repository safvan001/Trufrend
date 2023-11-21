from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from os.path import basename

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

class Profile(models.Model):
    phone_number = models.CharField(max_length=15,default=True)
    dp = models.ImageField(upload_to='img/profile_pictures', null=True, blank=True)
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50)
    challenges = models.ManyToManyField(Challenge)

    def __str__(self):
        return self.phone_number
class VideoPack(models.Model):
    video_file = models.FileField(upload_to='videos/',default=1)

    def __str__(self):
        return basename(str(self.video_file))
    # Add other fields if necessary

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_files = models.ManyToManyField(VideoPack)
    # Add other fields if necessary
    def __str__(self):
        return self.title
class Favorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)









# class VideoPack(models.Model):
#     title = models.CharField(max_length=100)
#     video_file = models.FileField(upload_to='videos/', default='')
#
# class Video(models.Model):
#     video_pack = models.ForeignKey(VideoPack, related_name='videos', on_delete=models.CASCADE,default=True)
#     description = models.TextField()
#     video_file = models.FileField(upload_to='videos/', default='')
