from common import *

########## DATABASE CONFIGURATION
import dj_database_url
DATABASES={}
DATABASES['default'] =  dj_database_url.config()
########## END DATABASE CONFIGURATION


########## LOGGING CONFIGURATION
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'catfacts.wsgi.application'
########## WSGI CONFIGURATION END