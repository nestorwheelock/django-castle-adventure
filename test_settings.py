"""
Minimal Django settings for running tests.
"""
SECRET_KEY = 'test-secret-key-for-castle-adventure'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'castle_adventure',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

USE_TZ = True
