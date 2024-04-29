import requests

from constants.urls import Urls


class UserDataActions:

    def get_authorized_user_data(self, token: str):
        response = requests.get(
            url=Urls.HOST + Urls.USER_BASE_PATH,
            headers={'Authorization': token}
        )
        return response


    def update_authorized_user_data(self, token: str, payload):
        response = requests.patch(
            Urls.HOST + Urls.USER_BASE_PATH,
            headers={'Authorization': token},
            data=payload
        )
        return response