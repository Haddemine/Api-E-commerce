from dataclasses import field
import imp
from rest_framework import serializers
from ecommerce import models

from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=User

class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Message

class ClientSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    class Meta:
        fields = '__all__'
        model=models.Client

class FournisseurSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
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
    fournisseurs = FournisseurSerializers(many=False)
    marqueprives = MarqueSerializers(many=False)
    categories =CategorieSerializers(many=False)
    class Meta:
        fields = '__all__'
        model=models.Produit
class CommandeSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Commande
class FavorisSerializers(serializers.ModelSerializer):
    produit=ProduitSerializers(many=False)
    class Meta:
        fields = '__all__'
        model=models.Favoris
        
class commandeitemSerializers(serializers.ModelSerializer):
    commande = CommandeSerializers(many=False)
    class Meta:
        fields = '__all__'
        model=models.Commandeitem       


class PanierSerializers(serializers.ModelSerializer):
    produit=ProduitSerializers(many=False)
    client=ClientSerializers(many=False)
    class Meta:
        fields = '__all__'
        model=models.Panier

class DemandeSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Demande
