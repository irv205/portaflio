from django.shortcuts import render
from django.conf.urls import url
from rest_framework import routers
from project.apps.security import views as secview
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

router = routers.DefaultRouter()

router.register(r'contact', views.ContactView, base_name='Contact')

urlpatterns = []

urlpatterns += router.urls