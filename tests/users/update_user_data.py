import allure
import pytest

from helper_functions.user_data_actions import UserDataActions


class UpdateUserData:


    @allure.title('Авторизация пользователя. Если передан некорректный логин или пароль, то авторизация неуспешна')
    @pytest.mark.parametrize(
        'missed_payload_field_key',
        ['name', 'email', 'password']
    )
    def test_update_user_data_with_valid_data_success(self, logged_user_access_token):
        use_data_actions = UserDataActions()

