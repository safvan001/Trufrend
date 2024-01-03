from django.db import models
from django.utils import timezone
from Trufrend.models import Profile
from AdminSide.models import DoctorData
class Feedback(models.Model):
    doctor=models.ForeignKey(DoctorData,on_delete=models.CASCADE)
    reason=models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.doctor)