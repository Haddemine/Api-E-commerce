from django.shortcuts import render
from ecommerce import models
from .serializers import ClientSerializers,FournisseurSerializers,CategorieSerializers,MarqueSerializers,ProduitSerializers
from rest_framework import generics

class ListClient(generics.ListCreateAPIView):
    queryset=models.Client.objects.all()
    serializer_class= ClientSerializers  

class DetailClient(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Client.objects.all()
    serializer_class= ClientSerializers   

class ListFournisseur(generics.ListCreateAPIView):
    queryset=models.Fournisseur.objects.all()
    serializer_class= FournisseurSerializers  

class DetailFournisseur(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Fournisseur.objects.all()
    serializer_class= FournisseurSerializers   

class ListCategorie(generics.ListCreateAPIView):
    queryset=models.Categorie.objects.all()
    serializer_class= CategorieSerializers  

class DetailCategorie(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Categorie.objects.all()
    serializer_class= CategorieSerializers 

class ListMarque(generics.ListCreateAPIView):
    queryset=models.MarquePrive.objects.all()
    serializer_class= MarqueSerializers  

class DetailMarque(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.MarquePrive.objects.all()
    serializer_class= MarqueSerializers 

class ListProduit(generics.ListCreateAPIView):
    queryset=models.Produit.objects.all()
    serializer_class= ProduitSerializers  

class DetailProduit(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Produit.objects.all()
    serializer_class= ProduitSerializers   
