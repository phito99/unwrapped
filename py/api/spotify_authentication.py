from typing import Json
import requests
import py.spotify_secret as spotify_secret
import base64


def get_access_token(auth_url: str, token_endpoint: str) -> str:
    try:
        ac_response: Json = requests.get(
            auth_url, params=spotify_secret.SPOTIFY_PARAMS).json()
        auth_code: str = ac_response["code"]
        token_headers: dict = {
            "Authorization": base64.b64encode(spotify_secret.SPOTIFY_CLIENT_ID + ":" + spotify_secret.SPOTIFY_CLIENT_SECRET),
            "Content-Type": "application/x-www-form-urlencoded"
        }
        token_body: dict = {
            "grant_type": "authorization_code",
            "code": auth_code
        }
        token_response = requests.post(
            token_endpoint, data=token_body, headers=token_headers)

    except:
        print(f"Failed")
        return None
