from ecommerce.models import Client,Fournisseur,Categorie,Service,Message,MarquePrive,Produit
from .serializers import ClientSerializers,FournisseurSerializers,CategorieSerializers,MarqueSerializers,ProduitSerializers
from rest_framework import generics
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.db.models import Q

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListClient(generics.ListCreateAPIView):    
    queryset=Client.objects.all()
    serializer_class = ClientSerializers

    # return Response(
    #     serializer.data,
    #     status=status.HTTP_200_OK
    # )
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailClient(generics.RetrieveUpdateDestroyAPIView):
    queryset=Client.objects.all()
    serializer_class= ClientSerializers   
    
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListFournisseur(generics.ListCreateAPIView):
    queryset=Fournisseur.objects.all()
    serializer_class= FournisseurSerializers  
    
    
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailFournisseur(generics.RetrieveUpdateDestroyAPIView):
    queryset=Fournisseur.objects.all()
    serializer_class= FournisseurSerializers   
    
    
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListCategorie(generics.ListCreateAPIView):
    queryset=Categorie.objects.all()
    serializer_class= CategorieSerializers  


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailCategorie(generics.RetrieveUpdateDestroyAPIView):
    queryset=Categorie.objects.all()
    serializer_class= CategorieSerializers 



@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListMarque(generics.ListCreateAPIView):
    queryset=MarquePrive.objects.all()
    serializer_class= MarqueSerializers  


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailMarque(generics.RetrieveUpdateDestroyAPIView):
    queryset=MarquePrive.objects.all()
    serializer_class= MarqueSerializers 


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListProduit(generics.ListCreateAPIView):
    queryset=Produit.objects.all()
    serializer_class= ProduitSerializers  


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailProduit(generics.RetrieveUpdateDestroyAPIView):
    queryset=Produit.objects.all()
    serializer_class= ProduitSerializers   


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def loginclient(request):

    uuu = request.data['username']
    ppp = request.data['password']
    try:
        u=authenticate(username=uuu,password=ppp)
    except:
        return Response(
            {
                'status': 'error',
                'message': 'no client for this information'
            },
            status.HTTP_200_OK
        )
        
    try:
        client = Client.objects.get(user=u)
        
        login(request,u)
        try:
            token = Token.objects.get(user=client.user)
        except:
            token = Token.objects.create(user=client.user)

        return Response(
            {
                'status': 'success',
                'token': str(token)
            },
            status.HTTP_200_OK
        )
    except:
        return Response(
            {
                'status': 'error',
                'message': 'no client for this information'
            },
            status.HTTP_200_OK
        )
        
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def registerclient(request):

    
        
    try:
        nom = request.data['nom']
        prenom = request.data['prenom']
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        telephone = request.data['telephone']
        sexe = request.data['sexe']
        description = request.data['description']
        adresse = request.data['adresse']
        user = User.objects.create_user(first_name=nom, last_name=prenom, email=email, username=username)
        user.set_password(password)
        user.save()
        client = Client.objects.create(user=user,telephone=telephone,sexe=sexe,description=description,adresse=adresse)
        client.save()
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
                'email': client.user.email,
                'nom': client.user.first_name,
                'prenom': client.user.last_name,
                'username': client.user.username,
                'telephone': client.telephone,
                'sexe': client.sexe,
                'description': client.description,
                'adresse': client.adresse
            },
            status.HTTP_200_OK
        )
    
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def loginfournisseur(request):

    uuu = request.data['username']
    ppp = request.data['password']
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
                'status': 'success',
                'token': str(token)
            },
            status.HTTP_200_OK
        )
    except:
        return Response(
            {
                'status': 'error',
                'message': 'no Frn for this information'
            },
            status.HTTP_200_OK
        )
        
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def home(request):
    
    tok=str(request.META.get('HTTP_AUTHORIZATION'))[6:]
    if len(tok)<1:
        return Response(
            {
                'message':'faut que vous connecter'
            },
            status.HTTP_200_OK
        )
    u = Token.objects.get(key=tok).user
    try:
        client = Client.objects.get(user=u)
        print(client)
    except:
        return Response(
            {
                'message':'client n existe pas'
            },
            status.HTTP_200_OK
        )
    return Response(
            {
                'email': client.user.email,
                'nom': client.user.first_name,
                'prenom': client.user.last_name,
                'username': client.user.username,
                'telephone': client.telephone,
                'sexe': client.sexe,
                'description': client.description,
                'adresse': client.adresse
            },
            status.HTTP_200_OK
        )
    