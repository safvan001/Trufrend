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

app_name="AdminSide"

urlpatterns = [
    path('Doctordetail/',DoctordatView.as_view(),name='doctordetail'),
    path('Doctordetail/<str:username>/', DoctorDataDetailView.as_view(), name='Doctordetail'),
    path('addlanguage/',AddLanguage.as_view(),name='addlanguage'),
    path('addspeciality/',AddSpecialization.as_view(),name='addspeciality'),
    # path('language/',LanguageView.as_view(),name='language'),
    # path('language/<int:pk>/',LanguageUpdateanddeletView.as_view(),name='language'),
    # path('specialization/',SpecializationView.as_view(),name='specialization'),
    # path('specialization/<int:pk>/',SpecializationUpdateandDeleteView.as_view(),name='upspecialization')
]
