from email.policy import default
from lib2to3.pgen2.token import COLONEQUAL
from operator import truediv
from tabnanny import verbose
from django.db import models

from django.db.models import Q
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=10)
    sexe = models.CharField(max_length=10)
    x = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    y  = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    image = models.ImageField(upload_to="", default="static/ecommerce/images/index.png",null=True)
    description = models.TextField(max_length=400, default="", editable=False)
    adresse = models.CharField(max_length=100, default="", editable=False)
    def __str__(self):
        return self.user.username

class Fournisseur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    status = models.CharField(max_length=20)
    nom_boutique = models.CharField(max_length=100)
    x = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    y  = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    def __str__(self):
        return self.user.first_name
    
class Service(models.Model):
    nom=models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom=models.CharField(max_length=100)
    image = models.ImageField(upload_to="", default="static/ecommerce/images/index.png", null=True)

    def __str__(self):
        return self.nom
    
class MarquePrive(models.Model):
    nom=models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
class Produit(models.Model):
     available= models.BooleanField(default=True)
     nom= models.CharField(max_length=200)
     prix = models.DecimalField(max_digits=10, decimal_places=2)
     quantite = models.IntegerField(max_length=100, default=1)
     description= models.CharField(max_length=200)
     fournisseurs= models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
     marqueprives= models.ForeignKey(MarquePrive, on_delete=models.CASCADE)
     categories= models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
     image=models.ImageField(upload_to='ecommerce/static/ecommerce/images',null=True)

     def __str__(self):
        return self.nom
    
class Commande(models.Model):
    description = models.CharField(max_length=500) 
    created_at = models.DateTimeField(auto_now_add=True)
    modePaiment = models.CharField(max_length=50) 
    statut = models.CharField(max_length=100) 
    client = models.ForeignKey(Client, related_name="sender", on_delete=models.CASCADE)
    
class Commandeitem(models.Model):
    commande = models.ForeignKey(Commande, related_name="commande", on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, related_name="sender", on_delete=models.CASCADE)
    quantite = models.IntegerField()
    etat = models.CharField(max_length=50, default="first")
    class Meta:
        verbose_name='Commandeitem'
        verbose_name_plural='Commandeitem'
    
class Message(models.Model):
     sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
     reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE)
     msg_content = models.CharField(max_length=500) 
     created_at = models.DateTimeField(auto_now_add=True)

class Favoris(models.Model):
    client = models.ForeignKey(Client, related_name="client", on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, related_name="produit", on_delete=models.CASCADE)
    def __str__(self):
        return self.produit.nom


class Panier(models.Model):
    client = models.ForeignKey(Client, related_name="cl", on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, related_name="pr", on_delete=models.CASCADE)
    quantite = models.IntegerField(blank=True)
    def __str__(self):
        return self.produit.nom

class Demande(models.Model):
    description = models.CharField(max_length=500) 
    created_at = models.DateTimeField(auto_now_add=True)
    modePaiment = models.CharField(max_length=50) 
    statut = models.CharField(max_length=100) 
    client = models.ForeignKey(Client, related_name="cli", on_delete=models.CASCADE)
    prixtotal=models.DecimalField(max_digits=10, decimal_places=2)
    ok=models.CharField(max_length=200,null=True)