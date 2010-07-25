import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'dev.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "public/static/")

MEDIA_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/base_admin/'

SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'chiplog_proj.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

CHIPLOG_MEDIA_URL = MEDIA_URL + 'chiplog/'
TEMPLATE_CONTEXT_PROCESSORS = (
    'chiplog.context_processors.chiplog_media_url',
    'django.contrib.auth.context_processors.auth',
)

INSTALLED_APPS = (
    'chiplog',
    'tagging',
    'typogrify',
    # 'django.contrib.redirects',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.humanize',
)

FORCE_LOWERCASE_TAGS = True

SESSION_COOKIE_NAME = 'chiplog'
