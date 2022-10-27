import os
import django
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ratn!684yf7ewt-%j%afwf7et9c=!oan$=w6#)fn#4u$ie4!as'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    '127.0.0.1'
]

# Application definition

INSTALLED_APPS = (
    # viewflow
    'viewflow.frontend',
    'viewflow',

    # material
    'material',
    'material.frontend',
    'material.admin',

    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'demo.bloodtest',
    'demo.customnode',
    'demo.leave',
    'demo.hr',
    'demo.countersign',
    'demo.integration',
    'demo.employees',
    'demo.testing',
    #'demo.shipment',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'material.frontend.middleware.SmoothNavigationMiddleware',
)

ROOT_URLCONF = 'demo.urls'

LOGIN_REDIRECT_URL = '/workflow/'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# import dj_database_url  # NOQA

# DATABASES = {
#     'default': dj_database_url.config() or {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db{}{}.sqlite3'.format(*django.VERSION[:2])),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sqlite3.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'demo/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'demo.website.users',
                'demo.website.testing_types',
                # 'material.frontend.context_processors.modules',
            ],
            'debug': True,
        },
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# South
if django.VERSION < (1, 7):
    INSTALLED_APPS += ('south', )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "demo", "static"),
]

# Whether to enable or not the StaticFilesHandler to serve the static resources from the WSGI
# server. Enabled by default if DEBUG = True, in production environmets it's recommended
# to serve the static resources with a reverse proxy like Nginx, unless little workloads
STATIC_ENABLE_WSGI_HANDLER = True

try:
    from demo.local_settings import *  # NOQA
except ImportError:
    pass


