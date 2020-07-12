"""
Django settings for quora project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't*996sd-hlbej1gmhb#$#55b6ih%$xvpdtm2wlh-=pap^2v7z4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL='accounts.MyUser'

CACHES={
    'default':{
        'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION':'127.0.0.1:11211',
    }
}


# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

   # 'memcache_status',

    'crispy_forms',
    'corsheaders',
    'rest_framework',
    

    'accounts.apps.AccountsConfig',
    'quans.apps.QuansConfig',
    'groups.apps.GroupsConfig',
    'actions.apps.ActionsConfig',
    'searching.apps.SearchingConfig',
    'api',
    #'channels',
    
    



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST=(
    'http://localhost:3000',
    'http://localhost:8000',
)


ROOT_URLCONF = 'quora.urls'

DEFAULT_RENDER_CLASSES=[
    'rest_framework.renderers.JSONRender',
]

if DEBUG:
    DEFAULT_RENDER_CLASSES+=[
        'rest_framework.renderers.BrowsableAPIRender',
    ]

#DEFAULT_RENDER_CLASSES=[
#    'rest_framework.renderers.JSONRender',
#]

#if DEBUG:
#    DEFAULT_RENDER_CLASSES

"""REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}"""

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

#ASGI_APPLICATION = 'quora.routing.application'#for channels

WSGI_APPLICATION = 'quora.wsgi.application'

#CHANNEL_LAYERS={
#    'default':{
#        'BACKEND':'channels_redis.core.RedisChannelLayer',
#        'CONFIG':{
#            'hosts':[('127.0.0.1', 6379)],
#        },
#    },
#}


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REDIS_HOST='localhost'
REDIS_PORT=6379
REDIS_DB=0

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_FINDERS=[
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]



MEDIA_ROOT=os.path.join(BASE_DIR, 'media')
MEDIA_URL='/media/'


LOGIN_REDIRECT_URL='home'
LOGOUT_REDIRECT_URL='home'
LOGIN_URL='login'
LOGOUT_URL='logout'


CRISPY_TEMPLATE_PACK='bootstrap4'
