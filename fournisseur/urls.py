from django.urls import path
from django.urls import re_path
from .views import *

app_name='ecommerce'

urlpatterns=[
    path('loginfournisseur/', loginfournisseur,name='loginfournisseur'),
    path('registerfournisseur/', registerfournisseur,name='registerfournisseur')
    
]