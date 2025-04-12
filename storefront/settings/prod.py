from .common import *



from .common import *
import os



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'rjcs_javac'
    }
}


ALLOWED_HOSTS = []

