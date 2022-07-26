from django.shortcuts import render
from ecommerce import models
from .serializers import ClientSerializers
from rest_framework import generics

class ListClient(generics.ListCreateAPIView):
    queryset=models.Client.objects.all()
    serializer_class= ClientSerializers  

class DetailClient(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Client.objects.all()
    serializer_class= ClientSerializers   
