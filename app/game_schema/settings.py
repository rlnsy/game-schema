"""
Django settings for game_schema project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mt*c(#x4k**ndmlwjsdj5-mm(hpv7g39l5za+_i0u=&-y1-)57'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEPLOYMENT_URL = "ERROR"
URL_PREFIX = "http"
URL_PORT = "ERROR"

with open("deployment.local.json") as f:
    params = json.loads(f.read())
    DEPLOYMENT_URL = params['url']
    if params['ssl']: URL_PREFIX="https"
    URL_PORT = params['port']
    DEBUG = params['debug']

BACKEND_URL = "%s://%s" % (URL_PREFIX, DEPLOYMENT_URL)
BACKEND_URL_WWW = "%s://www.%s" % (URL_PREFIX, DEPLOYMENT_URL)
FRONTEND_URL_BSC = "%s://%s" % (URL_PREFIX, DEPLOYMENT_URL)
FRONTEND_URL_WWW = "%s://www.%s" % (URL_PREFIX, DEPLOYMENT_URL)

ALLOWED_HOSTS = [
    "0.0.0.0", 
    "localhost", 
    BACKEND_URL, 
    BACKEND_URL_WWW,
    DEPLOYMENT_URL
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'games',
    'games.game_dice'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'game_schema.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'game_schema.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

CORS_ORIGIN_WHITELIST = [
    "http://0.0.0.0",
    "http://localhost",
    "http://127.0.0.1",
    "http://0.0.0.0:80",
    "http://localhost:80",
    "http://127.0.0.1:80",
    FRONTEND_URL_BSC,
    FRONTEND_URL_WWW
]
