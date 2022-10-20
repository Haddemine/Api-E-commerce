from datetime import datetime
from django.db.models import Count
from urllib import response
from ecommerce.models import Client, Commande, Demande, Favoris,Fournisseur,Categorie, Panier,Service,Message,MarquePrive,Produit, Commandeitem
from apis.serializers import ClientSerializers, CommandeSerializers, DemandeSerializers, FavorisSerializers,FournisseurSerializers,CategorieSerializers,MarqueSerializers, PanierSerializers,ProduitSerializers, UserSerializers, commandeitemSerializers
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.db.models import Q

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListUser(generics.ListCreateAPIView):    
    queryset=User.objects.all()
    serializer_class = UserSerializers



@api_view(['POST'])
def loginfournisseur(request):

    uuu = request.data['username']
    ppp = request.data['password']
    null=None
    try:
        u=authenticate(username=uuu,password=ppp)
    except:
        return Response(
            {
                'status': 'error',
                'message': 'no Frn for this information'
            },
            status.HTTP_200_OK
        )
        
    try:
        client = Fournisseur.objects.get(user=u)
        
        login(request, u)
        try:
            token = Token.objects.get(user=client.user)
        except:
            token = Token.objects.create(user=client.user)

        return Response(
            {
                'id':client.id,
                'status': True,
                'token': str(token),
                'message':'login success',
                'data':null
            },
            status.HTTP_200_OK
        )
    except:
        return Response(
            {
                'status': False,
                'message': 'no Frn for this information',
                'data': null
            },
            status.HTTP_200_OK
        )

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def registerfournisseur(request):   
    try:
        nom = request.data['nom']
        prenom = request.data['prenom']
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        telephone = request.data['telephone']
        image = request.FILES['image']
        nom_boutique = request.data['description']
        adresse = request.data['adresse']
        
        user = User.objects.create_user(first_name=nom, last_name=prenom, email=email, username=username)
        user.set_password(password)
        user.save()
        frn = Fournisseur.objects.create(user=user, telephone=telephone,image=image,nom_boutique=nom_boutique,adresse=adresse,status="Active")
        frn.save()
    except:
        return Response(
            {
                'status': 'error',
                'message': 'register failed'
            },
            status.HTTP_200_OK
        )
    return Response(
            {
                'email': frn.user.email,
                'nom': frn.user.first_name,
                'prenom': frn.user.last_name,
                'username': frn.user.username,
                'telephone': frn.telephone,
                'nom_boutique': frn.nom_boutique,
                'adresse': frn.adresse
            },
            status.HTTP_200_OK
        )
    
