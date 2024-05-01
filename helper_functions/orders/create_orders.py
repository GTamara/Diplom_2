from typing import Any

import requests
from requests import Response
import json

from constants.urls import Urls


class CreateOrders:

    @staticmethod
    def create_order(
        payload: dict[str, Any],
        token: str | None,
    ) -> Response:
        headers = {'Authorization': token} if token else {}
        response = requests.post(
            Urls.HOST + Urls.ORDER_BASE_PATH, # ORDER_BASE_PATH
            headers=headers,
            data=payload
        )
        # if response.status_code == 200:
        return response
        # raise Exception('Произошла ошибка при создании заказа')

    @staticmethod
    def get_ingredients() -> Response:
        response = requests.get(
            Urls.HOST + Urls.GET_INGREDIENTS_PATH,
        )
        if response.status_code == 200:
            return response
        raise Exception('Произошла ошибка при запросе ингредиентов')