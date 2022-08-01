from django.db import models

# Create your models here.

class User(models.Model):
    nom=models.CharField(max_length=100)
    nni=models.IntegerField()
    telephone=models.IntegerField()
    email=models.CharField(max_length=200)
    adresse=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    
class Client(User):

    def __str__(self):
        return self.nom

class Fournisseur(User):

    def __str__(self):
        return self.nom


    
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