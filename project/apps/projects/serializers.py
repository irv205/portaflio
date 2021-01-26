from rest_framework import serializers
from . import models
from project.apps.security.models import User

class ProjectsSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Projects
        fields = ('id', 'type', 'developer', 'name', 'description', 'main_features', 'references','photo')