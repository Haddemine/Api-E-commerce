from dataclasses import field
import imp
from rest_framework import serializers
from ecommerce import models


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Client

class FournisseurSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Fournisseur

class CategorieSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Categorie

class MarqueSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.MarquePrive

class ProduitSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Produit