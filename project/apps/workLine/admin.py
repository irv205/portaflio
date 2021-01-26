from django.contrib import admin
from .models import WorkLine

# Register your models here.
class WorkLineAdmin(admin.ModelAdmin):

    list_display = ('id', 'developer', 'name', 'description', 'job', 'date_start', 'date_end', 'functions')