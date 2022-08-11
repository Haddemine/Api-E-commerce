from distutils.debug import DEBUG
import os
from pathlib import Path
from environs import Env

env = Env() 
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "9UgT6gbc3LhFJTDJ-KnVTyCeAkVpdkWmrY9VYsCyBhA"

# DEBUG = env.bool("DEBUG", default=False)
DEBUG=True

ALLOWED_HOSTS = ['*','10.0.2.2','.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",
    "whitenoise.runserver_nostatic",
    
    
    'ecommerce',
    'apis',
    'cart',
    
    
    'rest_framework.authtoken',
    
    
    
    "drf_spectacular",
    'rest_framework',
    
    "allauth",
    "allauth.account", 
    "allauth.socialaccount", 
    "dj_rest_auth.registration",
    "dj_rest_auth"
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'superapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.request",
            ],
        },
    },
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SITE_ID = 1

WSGI_APPLICATION = 'superapp.wsgi.application'


DATABASES = {
"default": env.dj_db_url("DATABASE_URL") # new
}

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

REST_FRAMEWORK = {
    
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework.authentication.TokenAuthentication',
#    ),
#    'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#    ),
   "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
# "DEFAULT_PERMISSION_CLASSES": [
# "rest_framework.permissions.IsAuthenticated",
# ],
# "DEFAULT_AUTHENTICATION_CLASSES": [
# "rest_framework.authentication.SessionAuthentication",
# "rest_framework.authentication.TokenAuthentication", # new
# ],
# "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
"TITLE": "Blog API Project",
"DESCRIPTION": "A sample blog to learn about DRF",
"VERSION": "1.0.0",
# OTHER SETTINGS
}


LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "ecommerce/static")
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'ecommerce/media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_USE_JWT = True
