from django.contrib import admin
from ecommerce.models import  Client, Fournisseur, MarquePrive, Service, Categorie, Produit

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields=['nom']

@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    search_fields=['nom']
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields=['nom']
    
admin.site.register(MarquePrive)
admin.site.register(Categorie)
admin.site.register(Produit)