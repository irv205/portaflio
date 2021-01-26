from rest_framework import serializers
from . import models

class WorkLineSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.WorkLine
        fields = ('id', 'developer', 'name', 'description', 'job', 'date_start', 'date_end', 'functions')