from unicodedata import name
from django.urls import path

from apis.views import *



app_name='apis'
urlpatterns=[
    path('loginclient/', loginclient, name='loginclient'),
    path('registerclient/', registerclient, name='registerclient'),
    path('home/', home, name='home'),
    path('user/',ListUser.as_view(), name='listclient'),
    path('user/<int:pk>/',DetailUser.as_view()),
    path('demande/',ListDemande.as_view(), name='listclient'),
    path('demande/<int:pk>/',DetailDemande.as_view()),
    path('client/',ListClient.as_view(), name='listclient'),
    path('client/<int:pk>/',DetailClient.as_view()),
    path('fournisseur/',ListFournisseur.as_view(), name='listfournisseur'),
    path('fournisseur/<int:pk>/',DetailFournisseur.as_view()),
    path('message/',ListMessage.as_view(), name='listmessage'),
    path('message/<int:pk>/',DetailMessage.as_view()),
    
    #categorie
    path('produitcategorie/<int:categorieid>/', produitcategorie ,name='produitcategorie'),
    path('categorie/',ListCategorie.as_view(), name='listcategorie'),
    path('categorie/<int:pk>/',DetailCategorie.as_view()),
    
    
    #favoris
    path('MesFavoris/', MesFavoris ,name='MesFavoris'),
    
    path('ListFavoris/',ListFavoris.as_view(), name='ListFavoris'),
    path('DetailFavoris/<int:pk>/',DetailFavoris.as_view()),
    
    
    
    path('marque/',ListMarque.as_view(), name='listmarque'),
    path('marque/<int:pk>/',DetailMarque.as_view()),
    
    #produit
    path('produit/',ListProduit.as_view(), name='listproduit'),
    path('produit/<int:pk>/',DetailProduit.as_view()),
    path('detailplus/<int:idd>/', detailplus ,name='detailplus'),
    
    #commande
    
    path('lancercommande/', lancercommande ,name='lancercommande'),
    path('detailcommande/<int:idcmd>/', detailcommande, name='detailcommande'),
    path('commandesclient/', commandesclient, name='commandesclient'),
    path('commandesfournisseur/', commandesfournisseur, name='commandesfournisseur'),
    path('rechercheBoutiqueOuProduit/<str:key>/', rechercheBoutiqueOuProduit, name='rechercheBoutiqueOuProduit'),
    
    #panier
    
    path('lancerdemande/', lancerdemande ,name='lancerdemande'),
    path('panierclient/<int:clientid>/', panierclient ,name='panierclient'),
    path('addtopanier/<str:key>/',addtopanier,name='addtopanier'),
    path('addtofavoris/<str:key>/',addtofavoris,name='addtofavoris'),
    path('favorisclient/<int:clientid>/', favorisclient ,name='favorisclient'),
    path('deletefrompanier/<int:produitid>/', deletefrompanier ,name='deletefrompanier'),
    path('popular/',popular,name='popular'),

    path('messagefr/<int:id>/',messagefr,name='messagefr'),

    path('messagefrget/<int:id>/',messagefrget,name='messagefrget'),

    path('messageclientget/<int:id>/',messageclientget,name='messageclientget'),

    path('messageclient/<int:id>/',messageclient,name='messageclient')
    
    
    
]            