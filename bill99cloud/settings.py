"""
Django settings for bill99cloud project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+*@z0@yd)t1p3suwsw28dbwq-7sbpv_$ez4o#j!#w(35k12m8#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'UserManage'
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

ROOT_URLCONF = 'bill99cloud.urls'

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

WSGI_APPLICATION = 'bill99cloud.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ????????????
# import ldap
# from django_auth_ldap.config import LDAPSearch
#
# AUTHENTICATION_BACKENDS = (
#     'django_auth_ldap.backend.LDAPBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )
#
# '''???????????????
# AUTH_LDAP_SERVER_URI = "ldap://192.168.186.81:389"
# AUTH_LDAP_BIND_DN = "CN=secadmin01,OU=secadmin,OU=sec,OU=99BILLTEST,DC=99billtest,DC=com"
# AUTH_LDAP_BIND_PASSWORD = "99bill.com"
# AUTH_LDAP_USER_SEARCH = LDAPSearch("DC=99billtest,DC=com",ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
# '''
#
# AUTH_LDAP_SERVER_URI = "ldap://192.168.191.242:389"
# AUTH_LDAP_BIND_DN = "CN=sec_admin,OU=??????????????????,OU=99bill,DC=99bill,DC=com"
# AUTH_LDAP_BIND_PASSWORD = "8uhbCFT^"
# AUTH_LDAP_USER_SEARCH = LDAPSearch("DC=99bill,DC=com", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
#
# # AD????????????windows???????????????????????????
# AUTH_LDAP_CONNECTION_OPTIONS = {
#     ldap.OPT_DEBUG_LEVEL: 1,
#     ldap.OPT_REFERRALS: 0,
# }
#
# AUTH_LDAP_USER_ATTR_MAP = {
#     "username": "sAMAccountName",
#     "email": "userPrincipalName",
# }
#
# API_ACOUNT = {
#     'user':'SEC',
#     'pwd':'SEC@99bill.com'
# }

# ????????????
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {  # ????????????????????????handler????????????????????????????????????????????????????????????????????????
        'verbose': {  # ????????????
            # 2018-04-25 15:43:27,586 INFO views 8756 123145350217728 ??????????????????
            'format': '%(asctime)s [%(levelname)s] %(module)s %(message)s'
        },
        'simple': {
            # INFO  ??????????????????
            'format': '%(levelname)s %(message)s'
        },
        'standard': {
            # 2018-04-25 16:40:00,195 [Thread-7:123145575223296] [myapp.log:282] [views:user_query_json_get] [INFO]-
            # ??????????????????
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        },
    },
    "handlers": {  # ?????????????????????????????????,???????????????
        "console": {  # ??????????????????????????????
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # ?????????python???logging????????????StreamHandler???????????????
            'formatter': 'verbose'
        },
        'user_manage_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # ????????????,???????????????,????????????????????????????????????
            'filename': 'logs/user_manage.log',
            'maxBytes': 1024 * 1024 * 100,  # ????????????????????????,??????????????????100M
            'backupCount': 10,
            'formatter': 'verbose',
        },
        'others_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/others.log',
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 30,
            'formatter': 'verbose',
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/script.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 0,
            'formatter': 'verbose',
        },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/script.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 0,
            'formatter': 'verbose',
        },
    },
    "loggers": {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        "django_auth_ldap": {
            "level": "DEBUG",
            "handlers": ["console"]
        },
        'user_manage': {
            'handlers': ['user_manage_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'others': {
            'handlers': ['others_handler'],
            'level': 'INFO',
            'propagate': False
        },
    },
}
