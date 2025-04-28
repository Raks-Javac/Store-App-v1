from .common import *

# Add these at the top of your settings.py
import os

from decouple import config
import dj_database_url
DEBUG = True
SECRET_KEY = config('SECRET_KEY')
# REDIS_URL = os.environ['REDIS_URL']







DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
}





# CELERY_BROKER_URL = REDIS_URL


# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": REDIS_URL,
#         "TIMEOUT": 5 * 60,
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }


# DATABASES = {
#     'default': dj_database_url.config()
# }





# DATABASES = 

#    {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'storefront3',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': 'rjcs_javac'
#     }


ALLOWED_HOSTS = ['store-app-v1.onrender.com', 'oneshop.up.railway.app','127.0.0.1']

