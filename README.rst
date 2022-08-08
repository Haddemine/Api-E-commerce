ce projet est maintenant sur le domain : sup-er-app.herokuapp.com

pour runner ce projet en locale vous devez:

-pipenv shell
-pip install -r requirements.txt
-python -c "import secrets; print(secrets.token_urlsafe())"

après creer un fichier '.env'

ajouter : [

DEBUG=True
SECRET_KEY=votre sekret key
DATABASE_URL=sqlite:///db.sqlite3


]

les apis de partie rest_framework sont:

127.0.0.1:8000/api/dj-rest-auth/registration/

127.0.0.1:8000/api/dj-rest-auth/login

get<list> post get(id) update delete 

127.0.0.1:8000/apis/+[
    client
    client/id
    fournisseur
    fournisseur/id
    produit
    produit/id
    categorie
    categorie/id
    marque
    marque/id
]

127.0.0.1:8000/api/dj-rest-auth/logout

127.0.0.1:8000/api/dj-rest-auth/password/reset

127.0.0.1:8000/api/dj-rest-auth/password/reset/confirm

127.0.0.1:8000/api/schema/redoc/

127.0.0.1:8000/api/schema/swagger-ui/
