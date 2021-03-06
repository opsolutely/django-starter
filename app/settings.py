# Django settings for a generic project.
import os

ENVIRONMENT = os.environ.get('ENVIRONMENT')

DATABASES = {'default': {'NAME': '',
                         'ENGINE': 'django.db.backends.postgresql_psycopg2',
                         'USER': '',
                         'PASSWORD': '',
                         'HOST': 'localhost',
                         'PORT': ''}}
DEBUG = False
DEBUG_TOOLBAR = False

if ENVIRONMENT == 'dev':
    APP_BASE_LINK = 'http://127.0.0.1:5000'
    DEBUG = True
    DEBUG_TOOLBAR = True
    DATABASES['default']['NAME'] = 'project_db'

    def custom_show_toolbar(request):
        return True  # Always show toolbar, for example purposes only.

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
        'HIDE_DJANGO_SQL': False,
        'TAG': 'div',
        'ENABLE_STACKTRACES': True,
    }
elif ENVIRONMENT == 'production':
    APP_BASE_LINK = ''
    DATABASES['default']['NAME'] = 'project_db'
    DATABASES['default']['USER'] = 'db_user'
    DATABASES['default']['PASSWORD'] = os.environ.get('DB_PASSWORD')

TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
INTERNAL_IPS = ('127.0.0.1')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Project path
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
ROOT_PATH = BASE_DIR = os.path.join(os.path.dirname(__file__), '..')

# The application's base link.
APP_BASE_LINK = ''

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATIC_FILES = os.path.join(ROOT_PATH, 'static')
STATIC_BASE_LINK = APP_BASE_LINK + "/static/"
EXTRA_CONTEXT = {'static_base': STATIC_BASE_LINK,
                 'app_base_link': APP_BASE_LINK}

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(ROOT_PATH, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #  'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*lsatmymheaq)i+)80ryxau^^#uabdmtw&amp;1qhg9u-*cw_wmepn'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #  'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'app.wsgi.application'

TEMPLATE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'templates'))

TEMPLATE_DIRS = (
    TEMPLATE_DIR,
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'app',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_evolution',
    'djsupervisor',
    'gunicorn',
    'static',
    'templates'
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# Configuration for the email backend
SEND_BROKEN_LINK_EMAILS = True     # email us on all broken links
THROTTLE_OUTGOING_EMAIL = False
CACHE_RETRIES = 4

EMAIL_HOST = 'smtp.postmarkapp.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = os.environ.get('email_host_password')
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_PARAMS = {'host': EMAIL_HOST,
                     'username': EMAIL_HOST_USER,
                     'password': EMAIL_HOST_PASSWORD,
                     'fail_silently': False}

EMAIL_SUBJECT_PREFIX = "[%s] " % ''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # default config by Django but put explicitly
EMAIL_USE_TLS = True

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
