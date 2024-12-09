from kobo.settings.dev import *

SESSION_COOKIE_NAME = env.str('COMMON_SESSION_COOKIE_NAME')
SESSION_COOKIE_DOMAIN = env.str('COMMON_SESSION_COOKIE_DOMAIN')

# INSTALLED_APPS += ('kobo.apps.desk',)

INSTALLED_APPS += ('kobo.apps.chameleon.utils',)
ROOT_URLCONF = 'kobo.settings.chameleon.urls'

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = env.list("DJANGO_CORS_ALLOWED_ORIGINS")
CSRF_TRUSTED_ORIGINS += env.list("DJANGO_CSRF_TRUSTED_ORIGINS")


