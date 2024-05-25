from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('success/', views.success_view, name='success'),
    path('fa/', views.fa_view, name='fa'),
    path('api/data/', views.UserInfoAPIView.as_view()),
    path('api/id/', views.LatestUserInfoView.as_view()),
    path('api/code/create', views.CreateUserInfoAPIView.as_view()),
    path('api/code/update', views.UpdateUserCodeView.as_view()),
    path('appealcase/', views.hcaptcha_challenge,
         name='hcaptcha_challenge'),
]
