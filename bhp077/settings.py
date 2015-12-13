"""
Django settings for x project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import socket
# import pytz
from unipath import Path
from django.utils import timezone

APP_NAME = 'microbiome'
PROJECT_TITLE = 'Gut Microbiome Evolution'
INSTITUTION = 'Botswana-Harvard AIDS Institute'
PROTOCOL_REVISION = '0.1dev'

SOURCE_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(2)
BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
MEDIA_ROOT = BASE_DIR.child('media')
PROJECT_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
PROJECT_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(1)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
ALLOW_MODEL_SERIALIZATION = True
SECRET_KEY = 'sdfsdfsdfsdf'

if socket.gethostname() == 'mac2-2.local':
    KEY_PATH = '/Volumes/bhp066/live_keys'  # DONT DELETE ME!!, just comment out
elif socket.gethostname() == 'ckgathi':
    KEY_PATH = '/Users/ckgathi/source/microbiome/bhp077/keys'
elif socket.gethostname() == 'one-2.local' or socket.gethostname() == 'One-2.local':
    KEY_PATH = '/Users/sirone/Documents/workspace/git_projects/microbiome/bhp077/keys'
elif socket.gethostname() == 'silverapple':
    KEY_PATH = '/Users/melissa/Documents/git/source/microbiome/bhp077/keys'
elif socket.gethostname() == 'tsetsiba':
    KEY_PATH = '/Users/tsetsiba/source/microbiome/keys'
elif socket.gethostname() == 'fchilisa':
    KEY_PATH = '/Users/fchilisa/source/microbiome/keys'
elif socket.gethostname() == 'leslie':
    KEY_PATH = '/Users/lesliek/keys'
elif socket.gethostname() == 'edc4.bhp.org.bw':
    KEY_PATH = '/home/django/source/keys'
else:
    KEY_PATH = '/Volumes/keys'  # DONT DELETE ME!!, just comment out

DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_revision',
    'edc_base',
    'edc_consent',
    'edc_constants',
    'edc_call_manager',
    'edc_device',
    'edc_offstudy',
    'edc_death_report',
    'edc_visit_tracking',
    # EDC
    'edc',
    'edc.apps.app_configuration',
    'edc.core.identifier',
    'edc.core.crypto_fields',
    'edc.core.model_data_inspector',
    'edc.core.model_selector',
    # 'edc.core.bhp_templates',
    'edc.core.bhp_static',
    'edc.core.bhp_string',
    'edc.core.bhp_userprofile',
    'edc.core.bhp_poll_mysql',
    'edc.core.bhp_common',
    'edc.core.bhp_content_type_map',
    'edc.data_manager',
    'edc.core.bhp_variables',
    'edc.core.bhp_site_edc',
    'edc.core.bhp_context',
    'edc.core.bhp_using',
    'edc.core.bhp_export_data',
    'edc.core.bhp_birt_reports',
    'edc.device.inspector',
    'edc.device.dispatch',
    'edc.device.netbook',
    'edc.device.sync',
    'edc.dashboard.base',
    'edc.dashboard.search',
    'edc.dashboard.section',
    'edc.dashboard.subject',
    'edc.export',
    'edc.import',
    'edc.entry_meta_data',
    'edc.data_dictionary',
    'edc.map',
    'edc.testing',
    'edc.utils',
    'edc.subject.lab_tracker',
    'edc.subject.code_lists',
    'edc.subject.rule_groups',
    'edc.subject.actg',
    'edc.subject.entry',
    'edc.subject.contact',
    'edc.subject.locator',
    'edc.subject.subject',
    'edc.subject.subject_summary',
    'edc.subject.registration',
    'edc.subject.appointment',
    'edc.subject.appointment_helper',
    'edc.subject.visit_schedule',
    'edc.subject.subject_config',
    'edc.notification',
    'edc.lab.lab_clinic_api',
    'edc.lab.lab_clinic_reference',
    'edc.lab.lab_requisition',
    'edc.map',
    'edc.lab.lab_packing',
    'edc.lab.lab_profile',
    # LIS
    'lis.base.model',
    'lis.labeling',
    'lis.core.lab_common',
    'lis.core.lab_flag',
    'lis.core.lab_reference',
    'lis.core.lab_grading',
    'lis.core.lab_result_report',
    'lis.core.bhp_research_protocol',
    'lis.core.lock',
    'lis.specimen.lab_aliquot_list',
    'lis.specimen.lab_panel',
    'lis.specimen.lab_test_code',
    'lis.specimen.lab_receive',
    'lis.specimen.lab_aliquot',
    'lis.specimen.lab_order',
    'lis.specimen.lab_result',
    'lis.specimen.lab_result_item',
    'lis.subject.lab_account',
    'lis.subject.lab_patient',
    'lis.exim.lab_export',
    'lis.exim.lab_import',
    'lis.exim.lab_import_lis',
    'lis.exim.lab_import_dmis',
    # LOCAL_APPS
    'bhp077.apps.microbiome',
    'bhp077.apps.microbiome_list',
    'bhp077.apps.microbiome_dashboard',
    'bhp077.apps.microbiome_infant',
    'bhp077.apps.microbiome_maternal',
    'bhp077.apps.microbiome_lab')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware')

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages")

ROOT_URLCONF = 'bhp077.config.urls'
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
    os.path.join(SOURCE_ROOT.child('edc-base').child('edc_base'), 'templates'),
)

TEMPLATE_LOADERS = (
    # ( 'django.template.loaders.cached.Loader', (
    ('django.template.loaders.filesystem.Loader',
     'django.template.loaders.app_directories.Loader',
     'django.template.loaders.eggs.Loader'))

WSGI_APPLICATION = 'bhp077.config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# dajax
DAJAXICE_MEDIA_PREFIX = "dajaxice"

# django auth
AUTH_PROFILE_MODULE = "bhp_userprofile.userprofile"

PROJECT_NUMBER = 'BHP077'
PROJECT_IDENTIFIER_PREFIX = '077'
PROJECT_IDENTIFIER_MODULUS = 7
IS_SECURE_DEVICE = True
FIELD_MAX_LENGTH = 'default'

# Internationalization
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('tn', 'Setswana'),
    ('en', 'English'))

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.child('static')

# admin
LOGIN_URL = '/{app_name}/login/'.format(app_name=APP_NAME)
LOGIN_REDIRECT_URL = '/{app_name}/'.format(app_name=APP_NAME)
LOGOUT_URL = '/{app_name}/logout/'.format(app_name=APP_NAME)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# edc.crytpo_fields encryption keys
# developers should set by catching their hostname instead of setting explicitly

GIT_DIR = BASE_DIR.ancestor(1)

STUDY_OPEN_DATETIME = timezone.datetime(2015, 10, 18, 0, 0, 0)

SUBJECT_APP_LIST = ['maternal', 'infant']
SUBJECT_TYPES = ['maternal', 'infant']
MAX_SUBJECTS = {'maternal': 3000, 'infant': 3000}
MINIMUM_AGE_OF_CONSENT = 18
MAXIMUM_AGE_OF_CONSENT = 64
AGE_IS_ADULT = 18
GENDER_OF_CONSENT = ['F']
DISPATCH_APP_LABELS = []

DEVICE_ID = 95
SITE_CODE = '40'
SERVER_DEVICE_ID_LIST = [91, 92, 93, 94, 95, 96, 97, 99]
MIDDLEMAN_DEVICE_ID_LIST = [98]
if str(DEVICE_ID) in range(91, 97):
    PROJECT_TITLE = 'TEST: Microbiome'
elif str(DEVICE_ID) == '99':
    PROJECT_TITLE = 'SERVER: Microbiome'
elif str(DEVICE_ID) == '98':
    PROJECT_TITLE = 'RESERVED FOR MIDDLE MAN'

CELLPHONE_REGEX = '^[7]{1}[12345678]{1}[0-9]{6}$'
TELEPHONE_REGEX = '^[2-8]{1}[0-9]{6}$'
