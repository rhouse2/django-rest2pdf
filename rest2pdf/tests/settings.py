# Django settings for testapp project.
import os, sys
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR, TESTS = os.path.split(TEST_DIR)

#Ensure project is on system path.
sys.path.insert(0, TEST_DIR)
sys.path.append(APP_DIR)

DEFAULT_CHARSET = 'utf-8'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

test_engine = os.environ.get("REST2PDF_TEST_ENGINE", "sqlite3")

DATABASE_ENGINE = test_engine
DATABASE_NAME = os.environ.get("REST2PDF_DATABASE_NAME", "rest2pdf_test.db")
DATABASE_USER = os.environ.get("REST2PDF_DATABASE_USER", "")
DATABASE_PASSWORD = os.environ.get("REST2PDF_DATABASE_PASSWORD", "")
DATABASE_HOST = os.environ.get("REST2PDF_DATABASE_HOST", "localhost")

if test_engine == "sqlite":
    DATABASE_NAME = os.path.join(TEST_DIR, 'rest2pdf_test.db')
    DATABASE_HOST = ""
elif test_engine == "mysql":
    DATABASE_PORT = os.environ.get("REST2PDF_DATABASE_PORT", 3306)
elif test_engine == "postgresql_psycopg2":
    DATABASE_PORT = os.environ.get("REST2PDF_DATABASE_PORT", 5432)


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+r6lh5_(tb3eb50owmr)_---bl$fal+mjfx&f+qq-ib(+&x*@x'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'rest2pdf',
    'fakeapp',
)

# List of rst2pdf style sheet paths.
RST2PDF_STYLESHEET_DIRS = [os.path.join(APP_DIR,'styles'),]
