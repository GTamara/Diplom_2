import json

import allure
import requests
from requests import Response

from constants.urls import Urls


class LoginUser:

    @staticmethod
    # @allure.step('Логин пользователя с данными {user_login_valid_creds}')
    def login_user(payload: dict[str, str]) -> Response:
        response = requests.post(
            Urls.HOST + Urls.USER_LOGIN_PATH,
            data=json.dumps(payload),
            # data=payload,
            headers={
                'Content-Type': 'application/json; charset=utf-8'
            }
        )
        return response

    # @allure.step('Логин пользователя с данными {payload}')
    # def get_login_user_payload(self, user_login_valid_creds: dict[str, str]) -> Response:
    #     response = requests.post(
    #         Urls.HOST + Urls.USER_LOGIN_PATH,
    #         data=json.dumps(user_login_valid_creds),
    #         headers={
    #             'Content-Type': 'application/json; charset=utf-8'
    #         }
    #     )
    #     if response.status_code == 200:
    #         return response
    #     else:
    #         raise Exception('Произошла ошибка при авторизации пользователя')
    #
    # @allure.step('Получить логин пользователя')
    # def get_courier_id(self, login_creds: dict[str, str]) -> int:
    #     return self.login_courier(login_creds).json()['id']
