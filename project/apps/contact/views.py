from django.shortcuts import render
import json
from uuid import uuid4
from rest_framework import status
from rest_framework.views import Response, APIView
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import exceptions, permissions
from project.common.pagination import PageNumberPagination
from django.http import HttpResponse
from . import serializers
from . import models
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets, status, exceptions, permissions
from django.conf import settings
from django.shortcuts import get_object_or_404

# Create your views here.
class ContactView(viewsets.ModelViewSet):

    model = models.Contact
    permission_classes = ( )
    serializer_class = serializers.ContactSerializers

    def get_queryset(self):
        queryset = self.model.objects.all()
        return self.filter(queryset)  

    def filter(self, queryset):
        kwargs = self.request.GET
        name = kwargs.get('name', None)

        if name:
            queryset = queryset.filter(
                name = name
            )
            
        return queryset

    def perform_create(self, serializer):
        item = serializer.save()
        return item
    
    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
