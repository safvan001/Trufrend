
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from os.path import basename
from django.utils import timezone
# from AdminSide.models import DoctorData

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
class Languages(models.Model):
    language=models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.language

class Profile(models.Model):
    phone_number = models.CharField(max_length=15,default='')
    dp = models.ImageField(upload_to='img/profile_pictures', null=True, blank=True,default="img/profile_pictures/userimage.png")
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50)
    # DOB=models.DateField(null=True,blank=True)
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('others', 'others'),
    )
    Gender = models.CharField(max_length=100, choices=CHOICES, null=True, blank=True, default='Male')
    is_online = models.BooleanField(default=False)
    challenges = models.ManyToManyField(Challenge)
    language=models.ManyToManyField(Languages)
    videoFavour = models.ManyToManyField(Video)
    # from AdminSide.models import DoctorData
    from AdminSide.models import DoctorData
    doctorFavour=models.ManyToManyField(DoctorData, related_name='doctor_fav_profiles')
    # from AdminSide.models import DoctorData
    # recent_calls = models.ManyToManyField(DoctorData, related_name='recent_calls_of_user')

    def __str__(self):
        return self.phone_number
class Recent(models.Model):
    from AdminSide.models import DoctorData
    doctor=models.ForeignKey(DoctorData,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    time=models.DateTimeField(default=timezone.now, null=True, blank=True)
class Rating(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    from AdminSide.models import DoctorData
    doctor = models.ForeignKey(DoctorData,on_delete=models.CASCADE,default='')
    rating_value = models.IntegerField()

class Usercount(models.Model):
    user_count=models.IntegerField()
    def __int__(self):
        return self.user_count
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









