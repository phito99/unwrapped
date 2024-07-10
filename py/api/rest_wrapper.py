import requests
from types import Json, Response


class RestWrapper:
    """Class to use for making REST api requests"""

    def __init__(self, endpoint: str, hostname: str, headers: str, version: str) -> None:
        self.hostname: str = hostname
        self.endpoint: str = endpoint
        self.headers: dict = headers
        self.version: str = version
        self.url = f"https://api.{self.hostname}/{self.version}/{self.endpoint}"

    def _send_request(self, httpMethod: str) -> Response:
        json_response = requests.request(
            method=httpMethod, headers=self.headers, url=self.url)
        if json_response.status_code >= 200 and json_response.status_code < 300:
            return json_response.json()
        raise Exception(json_response.json()["message"])

    def get(self) -> Response:
        return self._send_request(method='GET')

    def post(self) -> Response:
        return self._send_request(method='POST')

    def put(self) -> Response:
        return self._send_request(method='PUT')

    def delete(self) -> Response:
        return self._send_request(method='DELETE')
