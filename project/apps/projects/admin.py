from django.contrib import admin
from .models import Projects

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):

    list_display = ('id', 'type', 'developer', 'name', 'description', 'main_features', 'references','photo')
    