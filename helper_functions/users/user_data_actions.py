import requests
from requests import Response

from constants.urls import Urls


class UserDataActions:

    @staticmethod
    def get_user_data(token: str) -> Response:
        headers = {'Authorization': token} if token else {}
        response = requests.get(
            url=Urls.HOST + Urls.USER_BASE_PATH,
            headers=headers
        )
        return response

    @staticmethod
    def update_user_data( payload: dict[str, str],token: str | None) -> Response:
        headers = {'Authorization': token} if token else {}
        response = requests.patch(
            Urls.HOST + Urls.USER_BASE_PATH,
            headers=headers,
            data=payload
        )
        return response