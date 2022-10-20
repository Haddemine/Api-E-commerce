from datetime import datetime
from django.db.models import Count
from urllib import response
from ecommerce.models import Client, Commande, Demande, Favoris,Fournisseur,Categorie, Panier,Service,Message,MarquePrive,Produit, Commandeitem
from .serializers import ClientSerializers, CommandeSerializers, DemandeSerializers, FavorisSerializers,FournisseurSerializers,CategorieSerializers,MarqueSerializers, MessageSerializers, PanierSerializers,ProduitSerializers, UserSerializers, commandeitemSerializers
from rest_framework import generics
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
from django.contrib.auth.models import User

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListUser(generics.ListCreateAPIView):    
    queryset=User.objects.all()
    serializer_class = UserSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializers  

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListClient(generics.ListCreateAPIView):    
    queryset=Client.objects.all()
    serializer_class = ClientSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailClient(generics.RetrieveUpdateDestroyAPIView):
    queryset=Client.objects.all()
    serializer_class= ClientSerializers   

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListFavoris(generics.ListCreateAPIView):    
    queryset=Favoris.objects.all()
    serializer_class = FavorisSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailFavoris(generics.RetrieveUpdateDestroyAPIView):
    queryset=Favoris.objects.all()
    serializer_class= FavorisSerializers



class ListDemande(generics.ListCreateAPIView):    
    queryset=Demande.objects.all()
    serializer_class = DemandeSerializers


class DetailDemande(generics.RetrieveUpdateDestroyAPIView):
    queryset=Demande.objects.all()
    serializer_class= DemandeSerializers   
    
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def MesFavoris(request):
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
        cli=Client.objects.get(user=u)
        fav = Favoris.objects.filter(client=cli)
    except:
        return Response(
            {
                'message': 'client mahu 5alg'
            },
            status.HTTP_200_OK
        )
    
    dataa = FavorisSerializers(fav, many=True)
    
    return Response(
        dataa.data,
        status.HTTP_200_OK
    )   
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

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListMessage(generics.ListCreateAPIView):    
    queryset=Message.objects.all()
    serializer_class = MessageSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailMessage(generics.RetrieveUpdateDestroyAPIView):
    queryset=Message.objects.all()
    serializer_class= MessageSerializers   

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def detailplus(request, idd):
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
        prod=Produit.objects.get(id=idd)
    except:
        return Response(
            {
                'message': 'produit mahu 5alg'
            },
            status.HTTP_200_OK
        )
    
    dataa = ProduitSerializers(prod, many=False)
    
    return Response(
        dataa.data,
        status.HTTP_200_OK
    )
    
    

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def loginclient(request):

    uuu = request.data['username']
    ppp = request.data['password']
    null=None
    try:
        u=authenticate(username=uuu,password=ppp)
    except:
        return Response(
            {
                'status': False,
                'message': 'no client for this information',
                'data': null
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
                'id':client.id,
                'status': True,
                'token': str(token),
                'message':'login success',
                'data':{
                    'telephone':client.telephone,
                    'sexe':client.sexe
                }
            },
            status.HTTP_200_OK
        )
    except:
        return Response(
            {
                'status': False,
                'message': 'no client for this information',
                'data': null
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
        # image= request.data['image']
        description = request.data['description']
        adresse = request.data['adresse']
        user = User.objects.create_user(first_name=nom, last_name=prenom, email=email, username=username)
        user.set_password(password)
        user.save()
        client = Client.objects.create(user=user, telephone=telephone,sexe=sexe,description=description,adresse=adresse)
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
                'image': client.image,
                'sexe': client.sexe,
                'description': client.description,
                'adresse': client.adresse
            },
            status.HTTP_200_OK
        )



@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def lancercommande(request):
    
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
    except:
        return Response(
            {
                'message':'client n existe pas'
            },
            status.HTTP_200_OK
        )
     
    desc = request.data['description']
    payment=request.data['payement']
    temp=datetime.now()
    c=Commande.objects.create(client=client,description=desc,modePaiment=payment,created_at=temp,statut="en cours")
    c.save()
    
    items = request.data['items']

    for item in items:
        idd=item['produit']
        q=item['quantite']
        prod=Produit.objects.get(id=idd)
        ci=Commandeitem.objects.create(commande=c,produit=prod,quantite=q)
        ci.save()
    
    return Response(
        {
            "message":"im coming mother fuckers"
        },
        status.HTTP_202_ACCEPTED
    )
   
    
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])   
def detailcommande(request,idcmd):
    try:
        cmd=Commande.objects.get(id=idcmd)
    except:
        return Response(
            {
                "message":"cmd doesn't exist"
            },
            status.HTTP_202_ACCEPTED
        )
    serializer = CommandeSerializers(cmd,many=False)
    cmditem=Commandeitem.objects.filter(commande=cmd)
    serializeritem = commandeitemSerializers(cmditem, many=True)
    dataa = {
        "commande":serializer.data,
        "commandeitem":serializeritem.data
    }
    return Response(
        dataa,
        status.HTTP_200_OK
    )
    
    
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])   
def commandesclient(request):
    tok=str(request.META.get('HTTP_AUTHORIZATION'))[6:]
    if len(tok)<1:
        return Response(
            {
                'message':'faut que vous connecter'
            },
            status.HTTP_200_OK
        )
    u = Token.objects.get(key=tok).user
    cl=Client.objects.get(user=u)
    commande= Commande.objects.filter(client=cl)
    serializer = CommandeSerializers(commande, many=True)   
    return Response(
        serializer.data,
        status.HTTP_200_OK
    )

    
    
   
def commandesfournisseur(request):
    tok=str(request.META.get('HTTP_AUTHORIZATION'))[6:]
    if len(tok)<1:
        return Response(
            {
                'message':'faut que vous connecter'
            },
            status.HTTP_200_OK
        )
    u = Token.objects.get(key=tok).user
    #get frn
    frn=Fournisseur.objects.get(user=u)
    #look if he has a cmditem in any cmd
    
    commande= Commande.objects.filter(fournisseur=frn)
    serializer = CommandeSerializers(commande, many=True)   
    return Response(
        serializer.data,
        status.HTTP_200_OK
    )
@api_view(['post'])
@permission_classes([])
@authentication_classes([])   
def rechercheBoutiqueOuProduit(request, key):
    frn=Fournisseur.objects.filter(nom_boutique__contains=key)
    frnser=FournisseurSerializers(frn, many=True)
    pro=Produit.objects.filter(Q(nom__contains=key) | Q(description__contains=key))
    proser=ProduitSerializers(pro, many=True)
    mydata={
        "fournisseurs":frnser.data,
        "produits":proser.data
    }
    return Response(
        mydata,
        status.HTTP_200_OK
    )
    
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])      
def produitcategorie(request, categorieid):
    try:
        cat = Categorie.objects.get(id=categorieid)
    except:
        return Response(
            {
                "message":"there is no categorie having this id bro"
            },
            status.HTTP_202_ACCEPTED
        )
    try:
        prod = Produit.objects.filter(categories=cat)
        products=ProduitSerializers(prod, many=True)
        return Response(
            products.data,
            status.HTTP_202_ACCEPTED
        )
    except:
        return Response(
            {
                "Unknown error happened, check ur data and try again"
            },
            status.HTTP_200_OK
        )
        
        
        
        
        
        




#-------------------------------------------------------------------------------------

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def addtopanier(request,key):
    
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
        produit=Produit.objects.get(nom=key)
    except:
        return Response(
            {
                'message':'client n existe pas'
            },
            status.HTTP_200_OK
        )
    client=client
    produit=produit
    quantite = request.data['quantite']
    c=Panier.objects.create(quantite=quantite,client=client,produit=produit)
    c.save()
    return Response(
        {
            "message":"Add successfully"
        },
        status.HTTP_202_ACCEPTED
    )
 
        
        
@api_view(['DELETE'])
@permission_classes([])
@authentication_classes([])      
def deletefrompanier(request, produitid): 
    try:
        produit = Produit.objects.get(id=produitid)
        panier = Panier.objects.filter(produit=produit)
    except:
        return Response(
            {
                "message":"there is no panier having this id bro"
            },
            status.HTTP_202_ACCEPTED
        )  
    try:
        panier.delete() 
        return Response(
            {
                "message":"Delete successfully"
            },
            status.HTTP_200_OK
        )
    except:
        return Response(
            {
                "Unknown error happened, check ur data and try again"
            },
            status.HTTP_200_OK
        )
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])      
def panierclient(request, clientid):
    try:
        client = Client.objects.get(id=clientid)
    except:
        return Response(
            {
                "message":"there is no client having this id bro"
            },
            status.HTTP_202_ACCEPTED
        )
    try:
        panier = Panier.objects.filter(client=client)
        paniers=PanierSerializers(panier, many=True)
        return Response(
            paniers.data,
            status.HTTP_202_ACCEPTED
        )
    except:
        return Response(
            {
                "Unknown error happened, check ur data and try again"
            },
            status.HTTP_200_OK
        )
        
        
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def lancerdemande(request):
    
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
    except:
        return Response(
            {
                'message':'client n existe pas'
            },
            status.HTTP_200_OK
        )
     
    desc = request.data['description']
    payment=request.data['payement']

    prixtotal=request.data['prixtotal']
    ok=request.data['ok']

    temp=datetime.now()
        
    c=Demande.objects.create(client=client,description=desc,modePaiment=payment,created_at=temp,statut="en cours",prixtotal=prixtotal,ok=ok)
    c.save()

    for item in items:
        idd=item['produit']
        q=item['quantite']
        prod=Produit.objects.get(id=idd)
        ci=Commandeitem.objects.create(commande=c,produit=prod,quantite=q)
        ci.save()
    
    return Response(
        {
            "message":"Commande successfully"
        },
        status.HTTP_202_ACCEPTED
    )
        


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def addtofavoris(request,key):
    
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
        produit=Produit.objects.get(nom=key)
    except:
        return Response(
            {
                'message':'client n existe pas'
            },
            status.HTTP_200_OK
        )
    client=client
    produit=produit
    c=Favoris.objects.create(client=client,produit=produit)
    c.save()
    return Response(
        {
            "message":"Add successfully"
        },
        status.HTTP_202_ACCEPTED
    )


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])      
def favorisclient(request, clientid):
    try:
        client = Client.objects.get(id=clientid)
    except:
        return Response(
            {
                "message":"there is no client having this id bro"
            },
            status.HTTP_202_ACCEPTED
        )
    try:
        favori = Favoris.objects.filter(client=client)
        favoris=FavorisSerializers(favori, many=True)
        return Response(
            favoris.data,
            status.HTTP_202_ACCEPTED
        )
    except:
        return Response(
            {
                "Unknown error happened, check ur data and try again"
            },
            status.HTTP_200_OK
        )


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])      
def popular(request):
    f=Favoris.objects.all().annotate(total=Count('produit')).order_by('-total')[:5]
    dataa = FavorisSerializers(f, many=True)
    return Response(
        dataa.data,
        status.HTTP_200_OK
        
    )



@api_view(['POST'])
@permission_classes([])
@authentication_classes([])      
def messageclient(request,id):
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
        fournisseur = Fournisseur.objects.get(id=id)
        msg=request.data['message']
    except:
        return Response(
            {
                'message':'client n existe pas'
            },
            status.HTTP_200_OK
        )
    c=Message.objects.create(sender=client.user,reciever=fournisseur.user,msg_content=msg,created_at=datetime.now())
    c.save()
    return Response(
        {
            "message":"message envoyé"
        },
        status.HTTP_202_ACCEPTED
    )



@api_view(['GET'])
@permission_classes([])
@authentication_classes([])      
def messageclientget(request,id):
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
        fournisseur = Fournisseur.objects.get(id=id)
        messagi=Message.objects.filter(sender=client.user.id,reciever=fournisseur.user.id)
        messago=Message.objects.filter(sender=fournisseur.user.id,reciever=client.user.id)
        MyResponse= MessageSerializers(messagi, many=True) 
        HisResponse= MessageSerializers(messago, many=True)
    except:
        return Response(
            {
                'message':'client n existe pas'
            },
            status.HTTP_200_OK
        )
    
    return Response(
        (MyResponse.data + HisResponse.data).order_by('-created_at'),
        status.HTTP_200_OK
    )

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])      
def messagefr(request,id):
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
        fournisseur = Fournisseur.objects.get(user=u)
        client = Client.objects.get(id=id)
        msg=request.data['message']
    except:
        return Response(
            {
                'message':'client n existe pas'
            },
            status.HTTP_200_OK
        )
    c=Message.objects.create(sender=fournisseur.user,reciever=client.user,msg_content=msg,created_at=datetime.now())
    c.save()
    return Response(
        {
            "message":"message envoyé"
        },
        status.HTTP_202_ACCEPTED
    )



@api_view(['GET'])
@permission_classes([])
@authentication_classes([])      
def messagefrget(request,id):
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
        fournisseur = Fournisseur.objects.get(user=u)
        client = Client.objects.get(id=id)
        messagi=Message.objects.filter(sender=fournisseur.user.id,reciever=client.user.id)
        messago=Message.objects.filter(sender=client.user.id,reciever=fournisseur.user.id)
        MyResponse= MessageSerializers(messagi, many=True) 
        HisResponse= MessageSerializers(messago, many=True)
    except:
        return Response(
            {
                'message':'client n existe pas'
            },
            status.HTTP_200_OK
        )
    
    return Response(
        (MyResponse.data + HisResponse.data).order_by('-created_at'),
        status.HTTP_200_OK
    )

