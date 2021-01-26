from rest_framework import serializers, exceptions
from . import models

class ContactSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Contact
        fields = ('id', 'name', 'email', 'message', 'job_offer')