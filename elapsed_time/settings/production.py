from elapsed_time.settings.base import *
import os

DEBUG = False


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'proje_adi',
        'USER': 'kullanici_adi',
        'PASSWORD': 'parola123',
        'HOST': 'localhost',
        'PORT': '',
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'static')