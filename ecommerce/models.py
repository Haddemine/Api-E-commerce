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
    
class Categorie(models.Model):
    nom=models.CharField(max_length=100)
    
class MarquePrive(models.Model):
    nom=models.CharField(max_length=100)