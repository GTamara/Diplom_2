import allure
import pytest

from constants.response_error_messages import ResponseErrorMessages
from helper_functions.users.login_user import LoginUser
from helper_functions.users.shared_helper_funcs import SharedHelperFuncs


class TestLoginUser:

    def test_login_user(self, user_login_valid_creds): # : dict[str, str]
        login = LoginUser()
        auth_data = user_login_valid_creds['auth_data']
        response = login.login_user(auth_data)
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert response.json()['success'] == True
        assert response.json()['user']['email'] == auth_data['email']
        assert response.json()['user']['name'] == auth_data['name']
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()

    @allure.title('Авторизация пользователя. Если передан некорректный логин или пароль, то авторизация неуспешна')
    @pytest.mark.parametrize(
        'missed_payload_field_key',
        [ 'email', 'password' ]
    )
    @pytest.mark.parametrize(
        'missed_payload_field_value',
        [
            '',
            SharedHelperFuncs().generate_random_email(10),
        ]
    )
    def test_login_user_with_with_not_all_required_params_fail(
            self,
            missed_payload_field_key,
            missed_payload_field_value,
            user_login_valid_creds
    ):
        login = LoginUser()
        auth_data = user_login_valid_creds['auth_data']
        login_payload = {
            **auth_data,
            missed_payload_field_key: missed_payload_field_value,
        }
        response = login.login_user(login_payload)
        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['message'] == ResponseErrorMessages.INCORRECT_LOGIN_DATA
