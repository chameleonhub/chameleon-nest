import json

from oauth2_provider.oauth2_validators import OAuth2Validator


class CustomOAuth2Validator(OAuth2Validator):
    # Set `oidc_claim_scope = None` to ignore scopes that limit which claims to return,
    # otherwise the OIDC standard scopes are used.
    # Extend the standard scopes to add a new "permissions" scope
    # which returns a "permissions" claim:

    oidc_claim_scope = OAuth2Validator.oidc_claim_scope
    oidc_claim_scope.update({"permissions": "permissions", "type": "type"})

    def get_additional_claims(self):
        return {
            "first_name": lambda request: request.user.first_name,
            "last_name": lambda request: request.user.last_name,
            "name": lambda request: ' '.join([request.user.first_name, request.user.last_name]),
            "username": lambda request: request.user.username,
            "email": lambda request: request.user.email,
            "permissions": lambda request: list(request.user.get_group_permissions()),
            "type": 'admin'
        }

    def get_userinfo_claims(self, request):
        claims = super().get_userinfo_claims(request)
        claims['username'] = request.user.username
        return claims
