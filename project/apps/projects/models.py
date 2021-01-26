from uuid import uuid4
from django.db import models
from django.conf import settings
from ...common.models import FieldDefaultsAbstracts
from django.utils.translation import ugettext as _
from project.apps.security.models import User
import os

def path_file_and_rename(obj, filename):
    ext = filename.split('.')[-1]

    filename = '{}.{}'.format(uuid4().hex, ext)
    path = 'projects/'
    return os.path.join(path, filename)

# Create your models here.
class Projects(FieldDefaultsAbstracts):

    type_project = (
        (1, _("Android")),
        (2, _("Web")),
        (3, _("Backend")),
        (4, _("IOS")),
        (5, _("Flutter")),
    )

    developer = models.ForeignKey(User, related_name="projects", blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    main_features = models.CharField(max_length=5000, blank=True, null=True)
    references = models.CharField(max_length=100, blank=True, null=True)
    photo = models.FileField(upload_to=path_file_and_rename, blank=True, null=True)
    type = models.IntegerField(choices=type_project, null=True, blank=True)

    def __str__(self):
        return self.developer.full_name

    class Meta:
        ordering = ['-id']

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args, **kwargs)
