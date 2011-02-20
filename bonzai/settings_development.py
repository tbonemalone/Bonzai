# Django settings for bonzi project.

from settings_local import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEFAULT_FROM_EMAIL = ''
SERVER_EMAIL = ''
EMAIL_SUBJECT_PREFIX = ''

SESSION_SAVE_EVERY_REQUEST=True

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en'
USE_I18N = False

SITE_ID = 1

ADMIN_MEDIA_PREFIX = '/admin-media/'

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'bonzai.urls'

TEMPLATE_DIRS = (
	join(LOCAL_PATH, 'templates')
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	# Uncomment the next line to enable the admin:
	'django.contrib.admin',
	'bonzai.seo_monitor',
)
