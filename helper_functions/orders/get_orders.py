import requests
from requests import Response

from constants.urls import Urls


class GetOrders:

    @staticmethod
    def get_user_orders(token: str | None) -> Response:
        headers = {'Authorization': token} if token else {}
        response = requests.get(
            Urls.HOST + Urls.GET_ORDERS_PATH,
            headers=headers,
        )
        return response


