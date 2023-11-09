from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

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

    def __str__(self):
        return self.challenges

class Profile(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    dp = models.ImageField(upload_to='img/profile_pictures', null=True, blank=True)
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50)
    challenges = models.ManyToManyField(Challenge)

    def __str__(self):
        return self.phone_number
class VideoPack(models.Model):
    title = models.CharField(max_length=100)
    # Add other fields if necessary
    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.ForeignKey(VideoPack, on_delete=models.CASCADE)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    # Add other fields if necessary
    def __str__(self):
        return self.title.title
