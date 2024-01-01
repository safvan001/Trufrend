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






urlpatterns = [
    path('api/intiate-user/', InitiateVerificationView.as_view(), name="initiate-verify"),
    path('api/verify-user/', VerifyUserView.as_view(), name='verify-user'),
    path('register/',ProfileListCreateAPIView.as_view(),name='register'),
    # path('view/',ProfileListAPIView.as_view(),name='view'),
    path('dp/',Dp.as_view(),name='dp'),
    path('update/<int:pk>/',UserUpdateAPIView.as_view(),name='update'),
    path('name/',Nickname.as_view(),name='name'),
    path('videos/',WellnessVideos.as_view(),name='video'),
    path('addchallenge/',AddChallenges.as_view(),name='addchallenge'),
    path('addlanguage/',AddLanguage.as_view(),name='AddLanguage'),
    path('challenge/',ChallengeList.as_view(),name='challenge'),
    path('addrecent/',RecentCallsofUser.as_view(),name='addrecent'),
    path('removerecent/',RemoveFromRecent.as_view(),name='removerecent'),
    # path('addrecent/',AddRecent.as_view(),name='addrecent'),
    # path('get_recent_doctors/<str:phone_number>/', GetRecentDoctors.as_view(), name='get_recent_doctors'),
    # path('get_profiles_by_doctor/<str:doctor_username>/', GetRecentProfile.as_view(), name='get_profiles_by_doctor'),
    # path('removerecent/',RemoveFromRecent.as_view(),name='removerecent'),
    path('usercount/',UserCount.as_view(),name='usecount'),
    path('setuserlive/',SetUserOnline.as_view(),name='setuserlive'),
    path('setuseroff/',SetUserOffline.as_view(),name='setuseroff'),
    path('onlineuser/',OnlineUserListView.as_view(),name='onlineuser'),
    # path('videos/<str:title>/',  VideoList.as_view(), name='video-list-create'),
    # path('video_packs/', VideoPackView.as_view(), name='video_pack_list'),
    path('Fvideo/',AddVideoFavouriteView.as_view(),name='Fvideo'),
    path('Fremove/',DeleteVideoFavouriteView.as_view(),name='Fremove'),
    path('Fdoctor/',AddDoctorFavourite.as_view(),name='Fdoctor'),
    path('Fremovedoctor/',RemoveDoctorFavourite.as_view(),name='Fremovedoctor'),
    path('rating/',AddRatingView.as_view(),name='rating'),
    path('showrating/',DoctorAverageRatingView.as_view(),name='showrating'),
    path('videotitle',Videotitle.as_view(),name='videotitle'),
    path('contactUs/', ContactUsCreateAPIView.as_view(), name='contactUs'),
    path('totalcount/',GetUserCountView.as_view(),name='totalcount'),
    path('get_user_profile/', get_user_profile.as_view(), name='get_user_profile'),
    path('Userdelete/',UserDelete.as_view(),name='Userdelete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)