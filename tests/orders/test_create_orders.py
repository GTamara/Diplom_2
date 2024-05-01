import allure

from constants.response_error_messages import ResponseErrorMessages
from helper_functions.orders.create_orders import CreateOrders
from helper_functions.users.shared_helper_funcs import SharedHelperFuncs


class TestCreateOrders:

    @allure.title('Создание заказа. Неавторизованный пользователь не может создать заказ')
    def test_create_order_for_unauthorized_user_fail(self, ingredients_list):
        create_order = CreateOrders()
        payload = {
            'ingredients': ingredients_list
        }
        response = create_order.create_order(
            payload,
            None
        )
        assert response.status_code == 401
        assert response.reason == 'Unauthorized'

    @allure.title('Создание заказа. Авторизованный пользователь может создать заказ с выбранными ингредиентами')
    def test_create_order_for_authorized_user_success(self, ingredients_list, logged_user_access_token):
        create_order = CreateOrders()
        payload = {
            'ingredients': ingredients_list
        }
        response = create_order.create_order(
            payload,
            logged_user_access_token
        )
        response_data = response.json()
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert response_data['success'] == True
        order_ingredients_list = SharedHelperFuncs().get_ingredients_list(
            response_data['order']['ingredients']
        )
        assert order_ingredients_list == ingredients_list

    @allure.title('Создание заказа. Авторизованный пользователь не может создать заказ с пустым списком ингредиентов')
    def test_create_order_for_empty_ingredients_list_fail(self, logged_user_access_token):
        create_order = CreateOrders()
        payload = {
            'ingredients': []
        }
        response = create_order.create_order(
            payload,
            logged_user_access_token
        )
        response_data = response.json()
        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert response_data['success'] == False
        assert response_data['message'] == ResponseErrorMessages.INGREDIENTS_MUST_BE_PROVIDED

    @allure.title('Создание заказа. Авторизованный пользователь может создать заказ с пустым списком ингредиентов')
    def test_create_order_with_incorrect_ingredient_hash_fail(self, ingredients_list, logged_user_access_token):
        create_order = CreateOrders()
        payload = {
            'ingredients': [
                ingredients_list[0] + SharedHelperFuncs().generate_random_string(5)
            ]
        }
        response = create_order.create_order(
            payload,
            logged_user_access_token
        )
        # response_data = response.json()
        assert response.status_code == 400
        assert response.reason == 'Bad Request'



