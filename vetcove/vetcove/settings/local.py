# Settings file that you use for when you're working on the project locally.
# ===========================================================================

from __future__ import absolute_import

from os.path import join, normpath

from .base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION
STATIC_DEBUG = DEBUG

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "vetcove",
#         "USER": "",
#         "PASSWORD": "",
#         "HOST": "localhost",
#         "PORT": "",
#     }
# }
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


###### Django Pipeline
# INSTALLED_APPS += (
#     'pipeline', # Django Pipeline for compression and minification of the CSS/JS files
# )
# STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

# PIPELINE_CSS = {
#     'colors': {
#         'source_filenames': (
#           'css/core.css',
#           'css/colors/*.css',
#           'css/layers.css'
#         ),
#         'output_filename': 'css/colors.css',
#         'extra_context': {
#             'media': 'screen,projection',
#         },
#     },
# }

# PIPELINE_JS = {
#     'stats': {
#         'source_filenames': (
#           'js/jquery.js',
#           'js/d3.js',
#           'js/collections/*.js',
#           'js/application.js',
#         ),
#         'output_filename': 'js/stats.js',
#     }
# }
####### End Django Pipeline


########## TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
# INSTALLED_APPS += (
#     'debug_toolbar',
# )

# MIDDLEWARE_CLASSES += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# )

#DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
########## END TOOLBAR CONFIGURATION

############# SECRET KEY
SECRET_KEY = 'wh3fk$t@(zt@ir!che_w)mo!#v$+n+9d&8(a1+8%51*flz!@h+'
############# END SECRET KEY
