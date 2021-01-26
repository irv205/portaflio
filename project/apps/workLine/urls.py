from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'work-line', views.WorkLineView, base_name="get work line")
router.register(r'get-work-line', views.GetWorkLineView, base_name="get work line no AUTH")

urlpatterns = []

urlpatterns += router.urls