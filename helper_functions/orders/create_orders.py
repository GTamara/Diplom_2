from typing import Any

import allure
import requests
from requests import Response

from constants.urls import Urls


class CreateOrders:

    @staticmethod
    @allure.step('Отправить запрос на создание заказа. Список ингредиентов {payload}')
    def create_order(
        payload: dict[str, Any],
        token: str | None,
    ) -> Response:
        headers = {'Authorization': token} if token else {}
        response = requests.post(
            Urls.HOST + Urls.ORDER_BASE_PATH,
            headers=headers,
            data=payload
        )
        return response

    @staticmethod
    @allure.step('Отправить запрос на получение ингредиентов')
    def get_ingredients() -> Response:
        response = requests.get(
            Urls.HOST + Urls.GET_INGREDIENTS_PATH,
        )
        if response.status_code == 200:
            return response
        raise Exception('Произошла ошибка при запросе ингредиентов')