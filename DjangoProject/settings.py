"""
Django settings for DjangoProject project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
#MEDIA_ROOT = "C:\Users\\ab32tx\Desktop\Bits 3-1\Python\DoctorsWebApp\Images"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR,'Images')
MEDIA_URL = '/images/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j23onn0g#5+d761e%&sq^h@t-14hr+hjmu3+7-ov@ji)z!r-fa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [u'med-4-u.appspot.com',u'192.168.10.15',u'127.0.0.1',u'192.168.1.104',u'192.168.10.16', u'192.168.10.20',u'192.168.10.25', u'192.168.43.46']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ProfileApp',    
    'GeneralApp',
    'MyHealthApp',
    'rest_framework',
    'django_cleanup',
    'django_filters',
    'social_django',
    # 'django-phonenumber-field'
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'DjangoProject.urls'

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
                'django.template.context_processors.media',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoProject.wsgi.application'


AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'dashboard'

SOCIAL_AUTH_TWITTER_KEY = 'V7bDYh8qyUOulwn2XaT859wC4'
SOCIAL_AUTH_TWITTER_SECRET = 'z8iSzJoEOkA4c3GxBdWcN7inuLlkIzftzWgr9ajn8VPudg1iw8'


SOCIAL_AUTH_FACEBOOK_KEY = '125359351382105'
SOCIAL_AUTH_FACEBOOK_SECRET = '3fd7cedb92b1434216c927c14b0efe2b'

# SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
# SOCIAL_AUTH_RAISE_EXCEPTIONS = False


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/med-4-u:us-central1:med-4-u',
            'NAME': 'doctors',
            'USER': 'root',
            'PASSWORD': '123456',
        }
    }
elif os.getenv('SETTINGS_MODE') == 'prod':
    # Running in development, but want to access the Google Cloud SQL instance
    # in production.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '35.188.97.205',
            'PORT': '',
            'NAME': 'doctors',
            'USER': 'root',
            'PASSWORD': '123456'
        }
    }
else:
    # Running locally so connect to either a local MySQL instance or connect to
    # Cloud SQL via the proxy. To start the proxy via command line:
    #
    #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:8000
    #
    # See https://cloud.google.com/sql/docs/mysql-connect-proxy
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '',
            'NAME': 'doctors',
            'USER': 'root',
            'PASSWORD': '123456',
        },
        'gcloud': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '35.188.97.205',
            'PORT': '',
            'NAME': 'doctors',
            'USER': 'root',
            'PASSWORD': '123456',
        }
    }


REST_FRAMEWORK = { 
'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',), 
'DEFAULT_RENDERER_CLASSES': ( 'rest_framework.renderers.JSONRenderer', 
                              'rest_framework.renderers.BrowsableAPIRenderer', ), 
'DEFAULT_AUTHENTICATION_CLASSES': ( 'rest_framework.authentication.TokenAuthentication', ), 
'DEFAULT_PERMISSION_CLASSES': ( 'rest_framework.permissions.AllowAny', ), 
}




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

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_ROOT = 'static'
STATIC_URL = '/static/'

AUTH_USER_MODEL = 'ProfileApp.Profile'

EMAIL_HOST = 'localhost'

EMAIL_PORT = 1025

PHONENUMBER_DB_FORMAT = 'E164'

DATE_FORMAT = ['%d/%m/%y']
