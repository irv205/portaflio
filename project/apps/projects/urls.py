from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'projects', views.ProjectsView, base_name="get projects")
router.register(r'get-projects', views.GetProjectView, base_name="get projects no AUTH")

urlpatterns = []

urlpatterns += router.urls