import allure
import requests
from requests import Response

from constants.urls import Urls
from helper_functions.users.shared_helper_funcs import SharedHelperFuncs


class RegisterUser:

    @staticmethod
    @allure.step('Сформировать тело запроса для регистрации курьера')
    def get_register_payload() -> dict[str, str]:
        helper_funcs = SharedHelperFuncs()
        email = helper_funcs.generate_random_email(10)
        password = helper_funcs.generate_random_string(8)
        name = helper_funcs.generate_random_string(5)
        return {
            'email': email,
            'password': password,
            'name': name
        }

    @staticmethod
    @allure.step('Запрос регистрации нового пользователя')
    def send_register_user_request(payload: dict[str, str]) -> Response:
        response = requests.post(Urls.HOST + Urls.USER_REGISTER_PATH, data=payload)
        return response

    @allure.step('Получить ответ на запрос регистрации нового пользователя')
    def get_register_user_payload(self) -> dict[str, str]:
        payload = self.get_register_payload()
        response = self.send_register_user_request(payload)
        if response.status_code == 200:
            return payload
        else:
            raise Exception('Произошла ошибка при регистрации пользователя')

