"""
Django settings for firstproject project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vfd5-^e61h7)2ocl$b5xd&lbybzp5hpjl_47g+1wo3#cyxd$v2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*' ,'16.170.219.193' , '172.31.39.63']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fisrtapp',
    # 'jet',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'firstproject.urls'

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

WSGI_APPLICATION = 'firstproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',#anything you want
        'USER': 'postgres', # username and pass which you defined in aws
        'PASSWORD': 'Database4',
        'HOST': 'database-4.cfy4mack4qov.eu-north-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[BASE_DIR/"static"]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    "site_title": "djnago project",
    "site_logo": "logo.jpeg",
    # "site_brand": "Library", 
    # or admin.site.site_header="Admin Header"
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "login_logo": "login.jpeg",
    "login_logo_dark": None,
    "welcome_sign": "Welcome to the Djangoworld",
    "copyright": "django admin Ltd",
    "search_model": ["auth.user", "auth.Group"],

    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["fisrtapp.view_user"]},
        {"name": "contact", "url": "https://www.linkedin.com/in/pallavi-sevak-6a602820a/", "new_window": False},
        {"model": "auth.User"},
    ],

    "usermenu_links": [
        {"name": "contact", "url": "https://www.linkedin.com/in/pallavi-sevak-6a602820a/", "new_window": False,"icon":"fas fa-phone-alt"},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,
    "navigation_expanded": False,
    # "hide_apps": ["fisrtapp"],
    # "order_with_respect_to": [],
    "custom_links": {
        "fisrtapp": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
        }]
    },

    # "default_icon_parents": "fas fa-chevron-circle-right",
    # "default_icon_children": "fas fa-circle",
    # "icons": {
    #     "fisrtapp": "fas fa-users-cog",
    #     "fisrtapp.user": "fas fa-user",
    #     "fisrtapp.Group": "fas fa-users",
    # },

    "show_ui_builder": True,
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "vertical_tabs",

}

# AWS_ACCESS_KEY_ID = 'AKIA47CRYIB7XNLU52OA '
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'buckettrial1'
# AWS_S3_SIGNATURE_NAME = 's3v4',
# AWS_S3_REGION_NAME = 'us-east-1'
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL =  None
# AWS_S3_VERITY = True
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
