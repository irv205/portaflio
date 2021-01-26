from uuid import uuid4
from django.db import models
from django.conf import settings
from ...common.models import FieldDefaultsAbstracts
from django.utils.translation import ugettext as _
from project.apps.security.models import User
import os

# Create your models here.
class WorkLine(FieldDefaultsAbstracts):

    developer = models.ForeignKey(User, related_name="work_line", blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    job = models.CharField(max_length=500, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    functions = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.developer.full_name

    class Meta:
        ordering = ['-id']
