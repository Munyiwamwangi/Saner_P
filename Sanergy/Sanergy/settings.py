"""
Django settings for Sanergy project.

Generated by 'django-admin startproject' using Django 1.11.27.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
# {% load crispy_forms_tags%}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dt4n@@q@uayg60$v-qyf@in-!hnks^!651oa41$9f17=-9cgr='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
db_host = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leave_management',
    'employee',
    'rest_framework',
    'bootstrap4',
    'bootstrap3',
    'social_django',
    'users',
    'crispy_forms',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Sanergy.urls'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}

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


CRISPY_TEMPLATE_PACK = 'bootstrap4'



WSGI_APPLICATION = 'Sanergy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'intranetsarnergy',
        'USER': 'intradmin',
        'PASSWORD': 'sanergy123',
        'HOST': 'localhost',
        'PORT': '5432',
    }


}

DATABASE_ROUTERS = [
    "salesforce.router.ModelRouter"
]

SALESFORCE_QUERY_TIMEOUT = (4, 15)  # default (connect timeout, data timeout)

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
AUTH_USER_MODEL = "employee.Employee"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
SITE_ID = 1

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

# salesforce credentials
SALESFORCE_USERNAME = 'domnick.kamya@saner.gy.ffa'
SALESFORCE_SECURITY_TOKEN = 'RolR1FqVokyPBjREIoBDq21j'
SALESFORCE_PASSWORD = 'Sanergy123'
SALESFORCE_DOMAIN = 'test'


# socoial auth setup
GOOGLE_OAUTH2_CLIENT_SECRETS_JSON = 'client_secrets.json'
SOCIAL_AUTH_POSTGRES_JSONFIELD = True

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1026629942419-qokhhup918dhbnmjfo21u5d2gdi9can3.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'qEQJSXwqbF0LiYIr5KVx2GKR'

LOGIN_URL = ''
PASSWORD_RESET_URL = 'password_reset'

LOGIN_REDIRECT_URL = 'landing'
LOGOUT_REDIRECT_URL = 'login'


'''
This error was due to the session cookie not being saved over a non-https url.
When testing on localhost with SESSION_COOKIE_SECURE set to True in django,
the session cookies will not persist between redirect and you will get this error in any kind of page change where session would be checked.
'''
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['state']
SESSION_COOKIE_SECURE = False



# Google email configurations:
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "domisemak@gmail.com"
EMAIL_HOST_PASSWORD = "Dommy2019"


