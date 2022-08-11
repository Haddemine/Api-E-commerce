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
        u=User.objects.get(username=uuu,password=ppp)
    except:
        return Response(
            {
                'status': 'error',
                'message': 'no client for this information'
            },
            status.HTTP_400_BAD_REQUEST
        )
        
    try:
        client = Client.objects.get(user=u)
        #login(request, u)
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
            status.HTTP_400_BAD_REQUEST
        )
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def loginfournisseur(request):

    uuu = request.data['username']
    ppp = request.data['password']
    try:
        u=User.objects.get(username=uuu,password=ppp)
    except:
        return Response(
            {
                'status': 'error',
                'message': 'no Frn for this information'
            },
            status.HTTP_400_BAD_REQUEST
        )
        
    try:
        client = Fournisseur.objects.get(user=u)
        #login(request, u)
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
            status.HTTP_400_BAD_REQUEST
        )