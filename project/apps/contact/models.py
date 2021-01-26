from uuid import uuid4
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from project.apps.security.models import User
import os

def path_file_and_rename(obj, filename):
    ext = filename.split('.')[-1]

    filename = '{}.{}'.format(uuid4().hex, ext)
    path = 'job_offer/'
    return os.path.join(path, filename)

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    message = models.CharField(max_length=255, blank=False, null=False)
    job_offer = models.FileField(upload_to=path_file_and_rename, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

    def delete(self, *args, **kwargs):
        self.job_offer.delete()
        super().delete(*args, **kwargs)