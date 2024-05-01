from helper_functions.orders.create_orders import CreateOrders
from helper_functions.orders.get_orders import GetOrders
from helper_functions.shared_helper_funcs import SharedHelperFuncs


class TestGetOrders:

    def test_get_authorized_user_orders(
        self,
        ingredients_list: list[str],
        logged_user_access_token: str
    ):
        create_order = CreateOrders()
        payload = {
            'ingredients': ingredients_list
        }
        create_order_response_data = create_order.create_order(
            payload,
            logged_user_access_token
        ).json()
        get_orders = GetOrders()
        response = get_orders.get_user_orders(logged_user_access_token)
        response_data = response.json()
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert response_data['success'] == True
        assert len(response_data['orders']) == 1
        assert response_data['orders'][0]['number'] == create_order_response_data['order']['number']
        assert response_data['orders'][0]['ingredients'] == \
            SharedHelperFuncs().get_ingredients_list(create_order_response_data['order']['ingredients'])
        assert response_data['orders'][0]['createdAt'] == create_order_response_data['order']['createdAt']

    def test_get_unauthorized_user_orders(self):
        get_orders = GetOrders()
        response = get_orders.get_user_orders(None)
        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['success'] == False
