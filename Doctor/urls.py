"""
URL configuration for Tru_frend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'stories', storiesView, basename='stories')
app_name="Doctor"
urlpatterns = [
    path('doctorlogin/',DoctorLoginView.as_view(),name='doctorlogin'),
    path('feedback/',DoctorFeedback.as_view(),name='DoctorFeedback'),
    path('counselorSchedule/',CounselorScheduling.as_view(),name='counselorSchedule'),
    path('counselorSchedule/get/<str:counselor_username>/', ScheduledCounselor.as_view(), name='counselorSchedule-get'),
    path('counselorreply/<int:schedule_id>/',CounselorReply.as_view(),name='CounselorReply'),
    path('counselorreply/get/<str:phone>/',GetCounselorReply.as_view(),name='CounselorReply'),
]

