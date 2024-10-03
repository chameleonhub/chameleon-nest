from kobo.settings.dev import *

SESSION_COOKIE_NAME = env.str('COMMON_SESSION_COOKIE_NAME')
SESSION_COOKIE_DOMAIN = env.str('COMMON_SESSION_COOKIE_DOMAIN')

# INSTALLED_APPS += ('kobo.apps.desk',)

INSTALLED_APPS += ('kobo.apps.bahis.utils',)
ROOT_URLCONF = 'kobo.settings.bahis.urls'

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")
CSRF_TRUSTED_ORIGINS += env.list("CSRF_TRUSTED_ORIGINS")


# OAUTH2_PROVIDER = {
#     "OIDC_ENABLED": True,
#     # "PKCE_REQUIRED": False,
#     "OIDC_RSA_PRIVATE_KEY": os.environ.get("OIDC_RSA_PRIVATE_KEY"),
#     "SCOPES": {
#         "openid": "OpenID Connect scope",
#         "profile": "Profile scope",
#         "email": "Email scope",
#         "read": "Read scope",
#         "write": "Write scope",
#         'introspection': 'Introspect token scope',
#         "address": "Address Scope",
#         "phone": "Phone Number Scope",
#         "permissions": "Permissions",
#         'type': 'User Type',
#         'groups': 'Access to your groups',
#     },
#     "OAUTH2_VALIDATOR_CLASS": "kobo.settings.bahis.oauth_validator.CustomOAuth2Validator",
#     "ACCESS_TOKEN_EXPIRE_SECONDS": 864000,
# }
