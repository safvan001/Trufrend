from django.db import models
from django.utils import timezone
from Trufrend.models import Profile
from AdminSide.models import DoctorData
class Feedback(models.Model):
    usernickname=models.CharField(max_length=50,default='')
    doctor=models.ForeignKey(DoctorData,on_delete=models.CASCADE)
    reason=models.TextField(null=True,blank=True)
    time=models.DateTimeField(default=timezone.now,blank=True)
    def __str__(self):
        return str(self.doctor)
class Schedule(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,default='')
    counselor = models.ForeignKey(DoctorData, on_delete=models.CASCADE,default='')
    date=models.DateTimeField(default=timezone.now, null=True, blank=True)
    message=models.TextField(null=True,blank=True)
    couselor_reply=models.TextField(blank=True,default='')

    def __str__(self):
        return str(self.user)