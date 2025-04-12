from .common import *



from .common import *
import os
import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default':dj_database_url.config()
}

os.environ.setdefault("DB_ENGINE", "django.db.backends.mysql")
os.environ.setdefault("DB_NAME", "storefront3")
os.environ.setdefault("DB_USER", "storefront3")
os.environ.setdefault("DB_PASSWORD", "rjcs_javac")
os.environ.setdefault("DB_HOST", "localhost")
os.environ.setdefault("DB_PORT", "3306")



#    {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'storefront3',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': 'rjcs_javac'
#     }


ALLOWED_HOSTS = ['store-app-v1.onrender.com', '*']

