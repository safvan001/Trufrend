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
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet)


urlpatterns = [
    path('api/intiate-user/', InitiateVerificationView.as_view(), name="initiate-verify"),
    path('api/verify-user/', VerifyUserView.as_view(), name='verify-user'),
    path('register/',ProfileListCreateAPIView.as_view(),name='register'),
    # path('view/',ProfileListAPIView.as_view(),name='view'),
    path('update/<int:pk>/',UserUpdateAPIView.as_view(),name='update'),
    path('name/',Nickname.as_view(),name='name'),
    path('age/',Age.as_view(),name='age'),
    path('sos/',CreateSOS.as_view(),name='sos'),
    path('addchallenge/',AddChallenges.as_view(),name='addchallenge'),
    path('usercount/',UserCount.as_view(),name='usecount'),
]
urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)