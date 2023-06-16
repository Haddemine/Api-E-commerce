from django.urls import path
from .views import index,indexcommerce,categorie,marque,addmarque,addmarquepost,addcategorie,addcategoriepost,produit,addproduit,addproduitpost,cart,detail
from django.urls import re_path

app_name='ecommerce'

urlpatterns=[
    # path('',index,name='index')
    path('indexcommerce',indexcommerce,name='indexcommerce'),
    path('categorie',categorie,name='categorie'),
    path('marque',marque,name='marque'),
    path('addmarque',addmarque,name='addmarque'),
    path('addmarquepost',addmarquepost,name='addmarquepost'),
    path('addcategorie',addcategorie,name='addcategorie'),
    path('addcategoriepost',addcategoriepost,name='addcategoriepost'),
    path('produit',produit,name='produit'),
    path('addproduit',addproduit,name='addproduit'),
    path('addproduitpost',addproduitpost,name='addproduitpost'),
    path('cart',cart,name='cart'),
    re_path(r'^(?P<produit_id>[0-9]+)/$',detail, name='detail')
]