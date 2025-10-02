"""
Development settings for running the dev server.
"""
from test_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

DEBUG = True
ALLOWED_HOSTS = ['*']
