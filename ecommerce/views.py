from email import message
from django.shortcuts import render,get_object_or_404
from ecommerce.models import  Client, Fournisseur, MarquePrive, Service, Categorie, Produit, Message
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.db import transaction, IntegrityError


from .models import Produit

# Create your views here.


def index(request):
    return render(request,'ecommerce/index.html')

def indexcommerce(request):
    produits_list=Produit.objects.filter(available=True)
    paginator = Paginator(produits_list, 9)
    page = request.GET.get('page')
    try:
        produits = paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)
    context={
        'produits': produits,
        'paginate': True
    }
    return render(request,'ecommerce/indexcommerce.html',context)

def categorie(request):
    categories=Categorie.objects.all()
    context={
        'categories': categories
    }
    return render(request,'ecommerce/categorie.html',context)

def marque(request):
    marques=MarquePrive.objects.all()
    context={
        'marques': marques
    }
    return render(request,'ecommerce/marque.html', context)

def addmarque(request):
    return render(request,'ecommerce/addmarque.html')

def addmarquepost(request):
    marques=MarquePrive.objects.all()
    context={
        'marques': marques
    }

    if request.method == 'POST':        
        nom= request.POST.get('nom')
        marqueprives=MarquePrive.objects.filter(nom=nom)
        if not marqueprives.exists():
                marqueprives = MarquePrive.objects.create(
                nom=nom
                )
        return render(request,'ecommerce/marque.html',context)
    return render(request,'ecommerce/marque.html',context)

def addcategorie(request):
    return render(request,'ecommerce/addcategorie.html')

def addcategoriepost(request):
    categories=Categorie.objects.all()
    context={
        'categories': categories
    }

    if request.method == 'POST':        
        nom= request.POST.get('nom')
        categories=Categorie.objects.filter(nom=nom)
        if not categories.exists():
                categories = Categorie.objects.create(
                nom=nom
                )
        return render(request,'ecommerce/categorie.html',context)
    return render(request,'ecommerce/categorie.html',context)

def produit(request):
    produits=Produit.objects.all()
    context={
        'produits': produits
    }
    return render(request,'ecommerce/produit.html', context)

def addproduit(request):
    fournisseurs=Fournisseur.objects.all()
    categories=Categorie.objects.all()
    marques=MarquePrive.objects.all()
    context={
        'fournisseurs': fournisseurs,
        'categories':categories,
        'marques':marques
    }
    return render(request,'ecommerce/addproduit.html',context)

def addproduitpost(request):
    produits=Produit.objects.all()
    context={
        'produits': produits
    }

    if request.method == 'POST':        
        nom= request.POST.get('nom')
        prix= request.POST.get('prix')
        description=request.POST.get('description')
        image= request.POST.get('image')
        categorie= request.POST.get('categorie')
        categorie=Categorie.objects.get(nom=categorie)
        marque= request.POST.get('marque')
        marque=MarquePrive.objects.get(nom=marque)
        fournisseur= request.POST.get('fournisseur')
        fournisseur=Fournisseur.objects.get(nom=fournisseur)
        produits=Produit.objects.filter(nom=nom)
        if not produits.exists():
                produits = Produit.objects.create(
                nom=nom,
                prix=prix,
                description=description,
                image=image,
                categories=categorie,
                marqueprives=marque,
                fournisseurs=fournisseur
                )
        return render(request,'ecommerce/produit.html',context)
    return render(request,'ecommerce/produit.html',context)

def cart(request):
    return render(request,'ecommerce/cart.html')



@transaction.atomic
def detail(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    # if request.method == 'POST':
    #     nom = request.POST.get('nom')
    #     nni = request.POST.get('nni')
    #     telephone=request.POST.get('telephone')
    #     email=request.POST.get('email')
    #     adresse=request.POST.get('adresse')
    #     try:
    #         with transaction.atomic():
    #             client = Client.objects.filter(nni=nni)
    #             if not client.exists():
    #                 client = Client.objects.create(
    #                     nom=nom,
    #                     nni=nni,
    #                     telephone=telephone,
    #                     email=email,
    #                     adresse=adresse
    #                 )
    #             else:
    #                 client = client.first()

    #             produit = get_object_or_404(Produit, id=produit_id)
    #             commande = Commande.objects.create(
    #                 client=client,
    #                 produit=produit
    #             )
    #             produit.available = False
    #             produit.save()
    #             context = {
    #                 'produit_title': produit.title
    #             }
    #             return render(request, 'GestionMg/merci.html', context)
    #     except IntegrityError:
    #         form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."


    context = {
        # 'produit_title': produit.title,
        'fournisseur': produit.fournisseurs,
        'prix': produit.prix,
        'img':produit.image,
        'produit_id': produit.id,
        'produit_image': produit.image,
        'nom':produit.nom,
        # 'form':form,
        # 'errors':form.errors.items()
    }
    return render(request, 'ecommerce/detail.html', context)

def reception(request):
    messages=Message.objects.filter(reciever=request.user)
    context={
        'messages':messages
    }
    return render(request, 'ecommerce/detail.html', context)

def envoyer(request):
    messages=Message.objects.filter(sender=request.user)
    context={
        'messages':messages
    }
    return render(request, 'ecommerce/detail.html', context)

