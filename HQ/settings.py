"""
Django settings for HQ project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, dj_database_url, logging

# logging.basicConfig(filename='test.log',level=logging.DEBUG)
# logging.debug('running logs...')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a)!((5zs3z$to9#!)x5s+p5!$#c6msc@0(#l3fuw@l=)&%0m%n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['mhq.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'HQ',
    'user',
    'tracker',
    'JQ'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'HQ.middleware.LoginRequiredMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'HQ.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'HQ.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tracker',
        'USER': 'rmooney',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
os.path.join(BASE_DIR, 'static'),
]
STATICFILES_FINDERS = [
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
'django.contrib.staticfiles.finders.FileSystemFinder',
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATIC_ROOT = './manage.py collectstatic'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'user/media')

LOGIN_URL = '/user/login/'
LOGIN_REDIRECT_URL = '/tracker/project/'

LOGIN_EXEMPT_URLS = {
    r'^user/home/$',
    r'^user/about/$',
    r'^user/contact/$',
    r'^user/signup/$',
    r'^user/reset-password/$',
    r'^user/reset-password/done/$',
    r'^user/reset-password/confirm/$',
    r'^user/reset-password/complete/$'
}

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
