import os

from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('ENGINE', default='django.db.backends.postgresql'),
        'NAME': os.environ.get('NAME', default='django_template'),
        'USER': 'postgres',
        'PASSWORD': os.environ.get('PASSWORD', default='hard_password_github_actions'),
        'HOST': os.environ.get('HOST', default='localhost'),
        'PORT': os.environ.get('PORT', default=5432),
    }
}