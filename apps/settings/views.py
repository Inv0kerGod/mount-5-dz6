from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Settings
from .serializers import *

# Create your views here.

class SettingsAPIView(ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class SettingsAPICreate(CreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsCreateSerializer

class SettingsAPIRetrieve(RetrieveAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsCreateSerializer

class SettingsAPIUpdate(UpdateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsCreateSerializer

class SettingsAPIDestroy(DestroyAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsCreateSerializer
