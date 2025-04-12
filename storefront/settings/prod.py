from .common import *



from .common import *
import os


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default':{
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ['MYSQL_DATABASE'],
#         'HOST': os.environ['MYSQLHOST'],
#         'USER': os.environ['MYSQLUSER'],
#         'PASSWORD': os.environ['MYSQLPASSWORD'],
#         'PORT': os.environ['MYSQLPORT'],  # Optional if default
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PGDATABASE'),
        'USER': os.getenv('PGUSER'),
        'PASSWORD': os.getenv('PGPASSWORD'),
        'HOST': os.getenv('PGHOST'),
        'PORT': os.getenv('PGPORT'),
        'OPTIONS': {
            'sslmode': 'require',  # Similar to MySQL's ssl_mode
        }
    }
}

REDIS_URL = os.environ['REDIS_URL']



CELERY_BROKER_URL = REDIS_URL


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "TIMEOUT": 5 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


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


ALLOWED_HOSTS = ['store-app-v1.onrender.com', '*']

