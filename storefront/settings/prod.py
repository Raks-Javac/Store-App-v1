from .common import *



from .common import *
import os
import dj_database_url
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']
REDIS_URL = os.environ['REDIS_URL']

DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
}







CELERY_BROKER_URL = REDIS_URL


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





# DATABASES = 

#    {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'storefront3',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': 'rjcs_javac'
#     }


ALLOWED_HOSTS = ['store-app-v1.onrender.com', 'oneshop.up.railway.app','127.0.0.1']

