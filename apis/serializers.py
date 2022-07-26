from dataclasses import field
import imp
from rest_framework import serializers
from ecommerce import models

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Client