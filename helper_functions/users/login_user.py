import json

import allure
import requests
from requests import Response

from constants.urls import Urls


class LoginUser:

    @staticmethod
    @allure.step('Логин пользователя с данными {payload}')
    def login_user(payload: dict[str, str]) -> Response:
        response = requests.post(
            Urls.HOST + Urls.USER_LOGIN_PATH,
            data=json.dumps(payload),
            headers={
                'Content-Type': 'application/json; charset=utf-8'
            }
        )
        return response
