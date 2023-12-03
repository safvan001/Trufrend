from django.contrib import admin
from AdminSide.models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(DoctorData)
admin.site.register(Languages)
admin.site.register(Specality)
# Register your models here.
