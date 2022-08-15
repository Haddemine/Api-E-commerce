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
    fournisseurs = FournisseurSerializers(many=False)
    marqueprives = MarqueSerializers(many=False)
    categories =CategorieSerializers(many=False)
    class Meta:
        fields = ('available','nom','prix','description','image','fournisseurs','categories','marqueprives')
        model=models.Produit
class CommandeSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Commande
        
class commandeitemSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.commandeitem       