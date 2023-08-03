from urllib.parse import urlencode
import requests
from starlette.responses import RedirectResponse

from settings import settings

"""
Client           CsInvest               Steam
  |   auth request   |                    |
  +------------------>                    |
  |                  |                    |
  | redirect response|                    |
  <------------------+                    |
  |                  |                    |
  | openid auth request                   |
  +------------------+-------------------->
  |                  |                    |
  | openid auth redirect response         |
  <------------------+--------------------+
  |                  |                    |
  | callback request |                    |
  +------------------>                    |
  |                  | validation request |
  |                  +-------------------->
  |                  |                    |
  |                  | validation response|
  |                  <--------------------+
  |jwt/refresh token |                    |
  <------------------+                    |
  |                  |                    |
"""

STEAM_OPENID_URL = 'https://steamcommunity.com/openid/login'
STEAM_OPENID_AUTH_PARAMS = urlencode({
    'openid.ns': 'http://specs.openid.net/auth/2.0',
    'openid.mode': 'checkid_setup',
    'openid.return_to': settings.APP_URL + '/auth/login/callback',
    'openid.realm': settings.APP_URL,
    'openid.identity': 'http://specs.openid.net/auth/2.0/identifier_select',
    'openid.claimed_id': 'http://specs.openid.net/auth/2.0/identifier_select'
})


def is_valid(oid_response: dict):
    oid_response.update({"openid.mode": "check_authentication"})
    response = requests.post(STEAM_OPENID_URL, data=oid_response)
    if "is_valid:true" in response.text:
        return True
    return False
