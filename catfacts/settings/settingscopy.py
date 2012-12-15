

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     'NAME': '',                      # Or path to database file if using sqlite3.
    #     'USER': '',                      # Not used with sqlite3.
    #     'PASSWORD': '',                  # Not used with sqlite3.
    #     'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    #     'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    # }
}


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c=6v)98#l6_igs=h9hf9s-yi%#zz#d1isuldksc$x@b+tdg7u7'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'catfacts.wsgi.application'



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

import dj_database_url
DATABASES['default'] =  dj_database_url.config()


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "catfacts_testing",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}
