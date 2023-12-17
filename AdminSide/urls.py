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
from rest_framework.routers import DefaultRouter

app_name="AdminSide"


urlpatterns = [
    path('Doctordetail/',DoctordatView.as_view(),name='doctordetail'),
    path('Doctordetail/<str:username>/', DoctorUpdateView.as_view(), name='doctor-detail'),
    path('addlanguage/',AddLanguage.as_view(),name='addlanguage'),
    path('addspeciality/',AddSpecialization.as_view(),name='addspeciality'),
    path('Fvideo/',DoctorVideoFavouriteView.as_view(),name='DoctorVideoFavour'),
    path('Fremove/',DeleteDrVideoFavouriteView.as_view(),name='fremove'),
    # path('story/',AllDoctorsWithStoriesView.as_view(),name='story'),
    path('getstory/',DoctorsWithStoriesAPIView.as_view(),name="getstory"),
    path('addstory/',AddStoryView.as_view(),name='addstory'),
    path('getallstory/',get_all_stories,name='getallstory'),
    path('quotes/',QuotesPostingView.as_view(),name='quotes'),
    path('setonline/',SetDoctorOnlineStatus.as_view(),name='doctorlive'),
    path('onlinedoctor/',OnlineDoctorListView.as_view(),name='onlinedoctor'),
    path('setoffline/',SetDoctorOffline.as_view(),name='setoffline')
    # path('language/',LanguageView.as_view(),name='language'),
    # path('language/<int:pk>/',LanguageUpdateanddeletView.as_view(),name='language'),
    # path('specialization/',SpecializationView.as_view(),name='specialization'),
    # path('specialization/<int:pk>/',SpecializationUpdateandDeleteView.as_view(),name='upspecialization')
]
