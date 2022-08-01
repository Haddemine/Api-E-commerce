from django.urls import path

from apis.views import DetailClient, ListClient, DetailFournisseur,ListFournisseur,ListCategorie,DetailCategorie,ListMarque,DetailMarque,ListProduit,DetailProduit

app_name='apis'
urlpatterns=[
    path('client',ListClient.as_view(), name='listclient'),
    path('client/<int:pk>/',DetailClient.as_view()),
    path('fournisseur',ListFournisseur.as_view(), name='listfournisseur'),
    path('fournisseur/<int:pk>/',DetailFournisseur.as_view()),
    path('categorie',ListCategorie.as_view(), name='listcategorie'),
    path('categorie/<int:pk>/',DetailCategorie.as_view()),
    path('marque',ListMarque.as_view(), name='listmarque'),
    path('marque/<int:pk>/',DetailMarque.as_view()),
    path('produit',ListProduit.as_view(), name='listproduit'),
    path('produit/<int:pk>/',DetailProduit.as_view())
]           