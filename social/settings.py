"""
Django settings for social project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MAIN_DIR = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_bf75$9p11_tl3i6#ok9z1_15amjr#^ozf6_8@2as^@r1t0mi8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'rest_framework',
    'pipeline',
)

INSTALLED_APPS += (
    'social',
    'people',
    'core',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'social.urls'

WSGI_APPLICATION = 'social.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(MAIN_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(MAIN_DIR, 'static'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

AUTH_USER_MODEL = 'people.SocialUser'


STATICFILES_FINDERS = (
    'pipeline.finders.FileSystemFinder',
    'pipeline.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'pipeline.finders.CachedFileFinder',
)


try:
    from local_settings import *
except ImportError:
    pass

PIPELINE = not DEBUG

PIPELINE_STORAGE = 'pipeline.storage.PipelineFinderStorage'

PIPELINE_CSS = {
    'libs': {
        'source_filenames': (
            'bower_components/angularjs/src/css/*.css',
        ),
        'output_filename': 'css/libs.min.css',
    },
    'app': {
        'source_filenames': (
            'css/app/*.css',
        ),
        'output_filename': 'css/app.min.css',
    }
}

PIPELINE_JS = {
    'libs': {
        'source_filenames': (
            'bower_components/angularjs/src/js/bootstrap.js',
        ),
        'output_filename': 'js/libs.min.js',
    },
    'app': {
        'source_filenames': (
            'js/app/*.js',
        ),
        'output_filename': 'js/app.min.js',
    }
}
