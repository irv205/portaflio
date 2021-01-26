from django.shortcuts import render
from rest_framework import status, exceptions, permissions, viewsets
from rest_framework.views import Response, APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from project.common.pagination import PageNumberPagination
from project.apps.security.models import User
from django.http import HttpResponse
from . import serializers, models
from django.conf import settings
import json

# Create your views here.
class WorkLineView(viewsets.ModelViewSet):

    model = models.WorkLine
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.WorkLineSerializers

    def get_queryset(self):
        queryset = self.model.objects.all()
        return self.filter(queryset)

    def filter(self, queryset):

        kwargs = self.request.GET
        id = kwargs.get('id', None)
        developer = kwargs.get('developer', None)

        queryset = queryset.filter(
            is_active = True
        )

        if id:
            queryset = queryset.filter(
                id = id
            )

        if developer:
            queryset = queryset.filter(
                developer = developer
            )
        
        return queryset

    def perform_create(self, serializer):

        item = serializer.save(
            owner = self.request.user,
            is_active=True       
        )
        return item
    
    def perform_update(self, serializer):
        serializer.save(
            is_active=True, 
        )

    def perform_destroy(self, instance):
        instance.delete() 
        
class GetWorkLineView(viewsets.ModelViewSet):

    model = models.WorkLine
    permission_classes = ( )
    serializer_class = serializers.WorkLineSerializers

    def get_queryset(self):
        queryset = self.model.objects.all()
        return self.filter(queryset)

    def filter(self, queryset):

        kwargs = self.request.GET
        id = kwargs.get('id', None)
        developer = kwargs.get('developer', None)

        queryset = queryset.filter(
            is_active = True
        )

        if id:
            queryset = queryset.filter(
                id = id
            )

        if developer:
            queryset = queryset.filter(
                developer = developer
            )
        
        return queryset