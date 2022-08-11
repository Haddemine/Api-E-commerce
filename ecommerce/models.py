from django.db import models

from django.db.models import Q
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=10)
    sexe = models.CharField(max_length=10)
    description = models.TextField(max_length=400, default="", editable=False)
    adresse = models.CharField(max_length=100, default="", editable=False)
    def __str__(self):
        return self.user.first_name

class Fournisseur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    status = models.CharField(max_length=20)
    nom_boutique = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name


    
class Service(models.Model):
    nom=models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom=models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
class MarquePrive(models.Model):
    nom=models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
class Produit(models.Model):
     available= models.BooleanField(default=True)
     nom= models.CharField(max_length=200)
     prix = models.DecimalField(max_digits=10, decimal_places=7)
     description= models.CharField(max_length=200)
     fournisseurs= models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
     marqueprives= models.ForeignKey(MarquePrive, on_delete=models.CASCADE)
     categories= models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
     image=models.ImageField(upload_to='ecommerce/static/ecommerce/images',null=True)

     def __str__(self):
        return self.nom

class Message(models.Model):
     sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
     reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE)
     msg_content = models.CharField(max_length=500) 
     created_at = models.DateTimeField(auto_now_add=True)