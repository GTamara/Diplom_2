from typing import Generator, Any

import pytest

from data.create_order_data import CreateOrderData
from helper_functions.delete_user import DeleteUser
from helper_functions.login_user import LoginUser
from helper_functions.register_user import RegisterUser
# from helper_functions.courier_helpers import CourierHelpers
# from helper_functions.login_courier import LoginCourier
# from helper_functions.order_helpers import OrderHelpers
# from helper_functions.register_courier import RegisterCourier
# from helper_functions.shared_helper_funcs import HelperFuncs


@pytest.fixture(scope="function")
def user_login_valid_creds() -> Generator[dict[str, str], Any, None]:
    register_user = RegisterUser()
    user_auth_data = register_user.get_register_user_payload()
    yield user_auth_data
    login_user = LoginUser()
    login_resp = login_user.login_user(user_auth_data) \
        .json()
    token = login_resp['accessToken']
    delete_user = DeleteUser()
    delete_user.delete_user(token)


@pytest.fixture(scope="function")
def user_login_valid_creds_1() -> Generator[dict[str, str], Any, None]:
    register_user = RegisterUser()
    user_auth_data = register_user.get_register_user_payload()
    login_user = LoginUser()
    login_resp = login_user.login_user(user_auth_data) \
        .json()
    token = login_resp['accessToken']
    yield {
        'auth_data': user_auth_data,
        'access_token': token
    }
    delete_user = DeleteUser()
    delete_user.delete_user(token)


@pytest.fixture(scope="function")
def logged_user_access_token() -> Generator[dict[str, str], Any, None]:
    register_user = RegisterUser()
    register_payload = register_user.get_register_user_payload()
    login_user = LoginUser()
    login_resp = login_user.login_user(register_payload) \
        .json()
    token = login_resp['accessToken']
    yield token
    delete_user = DeleteUser()
    delete_user.delete_user(token)


# @pytest.fixture(scope="function")
# def user__creds_иуфкук_ещлут() -> Generator[dict[str, str], Any, None]:
#     register_user = RegisterUser()
#     register_payload = register_user.get_register_user_payload()
#     register_payload.pop('name')
#     # login_user = LoginUser()
#     # login_resp = login_user.
#     yield register_payload
#     # courier_helpers = CourierHelpers()
#     # courier_helpers.delete_couriers_by_id(courier_id)
#

#
# send_login_user_request
#

# @pytest.fixture(scope="function")
# def courier_valid_login_and_incorrect_password(courier_login_valid_creds):
#     return {
#         'login': courier_login_valid_creds[0]['login'],
#         'password': HelperFuncs.generate_random_string(8)
#     }
#
#
# @pytest.fixture(scope="function")
# def courier_valid_password_and_incorrect_login(courier_login_valid_creds):
#     return {
#         'password': courier_login_valid_creds[0]['password'],
#         'login': HelperFuncs.generate_random_string(8)
#     }
#
#
# @pytest.fixture(
#     scope="function",
#     params=['courier_valid_login_and_incorrect_password', 'courier_valid_password_and_incorrect_login']
# )
# def courier_login_valid_login_and_password(request):
#     return request.getfixturevalue(request.param)
#
#
# @pytest.fixture(scope="function")
# def created_order_data():
#     order_helpers = OrderHelpers()
#     payload = {
#         **CreateOrderData.DEFAULT_CREATE_ORDER_PAYLOAD,
#         'phone': HelperFuncs.generate_random_phone(),
#         'deliveryDate': HelperFuncs.get_tomorrow_date()
#     }
#     resp = order_helpers.create_order_request(CreateOrderData.DEFAULT_CREATE_ORDER_PAYLOAD)
#     order_track = order_helpers.get_order_track(resp)
#     order_data = order_helpers.get_order_data(order_track)
#     yield (order_track, order_data)
#     order_helpers.cancel_order(order_track)
