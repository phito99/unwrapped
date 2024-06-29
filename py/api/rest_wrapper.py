import requests
from types import Json, Response


class RestWrapper:
    """Class to use for making REST api requests"""

    def __init__(self, endpoint: str, base_url: str, headers: str, token: str) -> None:
        self.base_url: str = base_url
        self.token: str = token
        self.endpoint: str = endpoint
        self.headers: dict = headers

    def _send_request(httpMethod: str) -> Response:
        json_response = requests.request(
            method=httpMethod, headers=self.headers, url=(self.url + self.endpoint))
        if json_response.status_code >= 200 and json_response.status_code < 300:
            return json_response.json()
        raise Exception(json_response.json()["message"])

    def get():
        return self._send_request(method='GET')

    def post():
        return self._send_request(method='POST')

    def put():
        return self._send_request(method='PUT')

    def delete():
        return self._send_request(method='DELETE')
