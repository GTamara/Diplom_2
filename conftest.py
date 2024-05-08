from typing import Generator, Any
import pytest

from helper_functions.orders.create_orders import CreateOrders
from helper_functions.users.delete_user import DeleteUser
from helper_functions.users.login_user import LoginUser
from helper_functions.users.register_user import RegisterUser
from helper_functions.shared_helper_funcs import SharedHelperFuncs


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
def user_login_valid_creds_and_token() -> Generator[dict[str, str | dict[str, str]], Any, None]:
    register_user = RegisterUser()
    user_auth_data = register_user.get_register_user_payload()
    login_user = LoginUser()
    login_resp = login_user.login_user(user_auth_data).json()
    token: str = login_resp['accessToken']
    yield {
        'auth_data': user_auth_data,
        'access_token': token
    }
    delete_user = DeleteUser()
    delete_user.delete_user(token)


@pytest.fixture(scope="function")
def logged_user_access_token() -> Generator[Any, Any, None]:
    register_user = RegisterUser()
    register_payload = register_user.get_register_user_payload()
    login_user = LoginUser()
    login_resp = login_user.login_user(register_payload) \
        .json()
    token = login_resp['accessToken']
    yield token
    delete_user = DeleteUser()
    delete_user.delete_user(token)


@pytest.fixture(scope="function")
def ingredients_list() -> list:
    create_orders = CreateOrders()
    response_data = create_orders.get_ingredients().json()['data']
    ingredients_list = SharedHelperFuncs.get_ingredients_list(response_data)
    return ingredients_list
