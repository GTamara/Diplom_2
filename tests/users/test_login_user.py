import allure
import pytest

from constants.response_error_messages import ResponseErrorMessages
from helper_functions.login_user import LoginUser
from  helper_functions.shared_helper_funcs import SharedHelperFuncs


class TestLoginUser:

    def test_login_user(self, user_login_valid_creds): # : dict[str, str]
        login = LoginUser()
        response = login.login_user(user_login_valid_creds)
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert response.json()['success'] == True
        assert response.json()['user']['email'] == user_login_valid_creds['email']
        assert response.json()['user']['name'] == user_login_valid_creds['name']
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
            SharedHelperFuncs().generate_email(10),
        ]
    )
    def test_login_user_with_with_not_all_required_params_fail(
            self,
            missed_payload_field_key,
            missed_payload_field_value,
            user_login_valid_creds):
        login = LoginUser()
        login_payload = {
            **user_login_valid_creds,
            missed_payload_field_key: missed_payload_field_value,
        }
        response = login.login_user(login_payload)
        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['message'] == ResponseErrorMessages.INCORRECT_LOGIN_DATA
