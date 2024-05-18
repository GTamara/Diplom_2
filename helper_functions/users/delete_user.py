import allure
import requests
from requests import Response

from constants.urls import Urls


class DeleteUser:

    @staticmethod
    @allure.step('Удалить юзера')
    def delete_user(token: str) -> Response:
        url = Urls.HOST + Urls.USER_BASE_PATH
        return requests.delete(
            url=url,
            headers={'Authorization': token}
        )