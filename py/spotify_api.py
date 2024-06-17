import requests
import secrets


BASE_URL = "https://api.spotify.com"


class SpotifyWrapper:

    def __init__(self, token, endpoint, base_url=BASE_URL) -> None:
        if self.base_url is not None:
            self.base_url = base_url 
        self.token = token
        self.endpoint = endpoint
    
    def _create_header():
       header = {
           
           
       } 

    def _send_request():
        pass

    def get():
        pass

    def post():
        pass

    def put():
        pass

    def delete():
        pass

