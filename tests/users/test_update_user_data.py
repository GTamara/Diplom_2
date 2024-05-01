from typing import Generator, Any

import allure
import pytest

from constants.response_error_messages import ResponseErrorMessages
from helper_functions.users.shared_helper_funcs import SharedHelperFuncs
from helper_functions.users.user_data_actions import UserDataActions


class TestUpdateUserData:

    @allure.title('Изменение данных пользователя пользователя. Изменение поля {field_to_update} успешно')
    @pytest.mark.parametrize(
        'field_to_update',
        ['name', 'email', 'password']
    )
    def test_update_authorized_user_data_with_valid_data_success(self, field_to_update, logged_user_access_token):
        use_data_actions = UserDataActions()
        get_data_response = use_data_actions.get_user_data(logged_user_access_token) \
            .json()
        new_field_value = SharedHelperFuncs().generate_random_email(10)
        update_data_payload = {
            **get_data_response['user'],
            field_to_update: new_field_value
        }
        update_data_response = use_data_actions.update_user_data(
            update_data_payload,
            logged_user_access_token
        )
        assert update_data_response.status_code == 200
        assert update_data_response.reason == 'OK'
        assert update_data_response.json()['success'] == True
        assert update_data_response.json()['user']['email'] == update_data_payload['email']
        assert update_data_response.json()['user']['name'] == update_data_payload['name']
        assert 'password' not in  update_data_response.json()['user']

    @allure.title('Изменение данных пользователя пользователя. Изменение поля {field_to_update} успешно')
    @pytest.mark.parametrize(
        'field_to_update',
        ['name', 'email', 'password']
    )
    def test_update_unauthorized_user_data_with_valid_data_fail(self, field_to_update, logged_user_access_token):
        use_data_actions = UserDataActions()
        # получить данные юзера перед попыткой обновления данных
        response_data_before_updating = use_data_actions.get_user_data(logged_user_access_token) \
            .json()
        new_field_value = SharedHelperFuncs().generate_random_email(10)
        update_data_payload = {
            **response_data_before_updating['user'],
            field_to_update: new_field_value,
        }
        # попытка обновления данных
        update_data_response = use_data_actions.update_user_data(
            update_data_payload,
            None
        )
        update_data_response_json = update_data_response.json()
        assert update_data_response.status_code == 401
        assert update_data_response.reason == 'Unauthorized'
        assert update_data_response_json['success'] == False
        assert update_data_response_json['message'] == ResponseErrorMessages.NOT_AUTHORIZED
        assert 'user' not in update_data_response_json
        # получить данные юзера после попытки обновления данных и проверка, что данные не изменились
        response_data_after_updating = use_data_actions.get_user_data(logged_user_access_token) \
            .json()
        assert response_data_after_updating['user']['name'] \
               == response_data_before_updating['user']['name']
        assert response_data_after_updating['user']['email'] \
               == response_data_before_updating['user']['email']

    def test_register_user_with_used_email_fail(
        self,
        user_login_valid_creds: dict[str, str],
        logged_user_access_token: str
    ):
        use_data_actions = UserDataActions()
        # получить данные юзера перед попыткой обновления данных
        response_data_before_updating = use_data_actions.get_user_data(logged_user_access_token) \
            .json()
        update_data_payload = {
            **response_data_before_updating,
            'email': user_login_valid_creds['auth_data']['email']
        }
        update_data_response = use_data_actions.update_user_data(
            update_data_payload,
            logged_user_access_token
        )
        assert update_data_response.status_code == 403
        assert update_data_response.reason == 'Forbidden'
        assert update_data_response.json()['success'] == False
        assert update_data_response.json()['message'] == ResponseErrorMessages.EMAIL_ALREADY_IN_USE
        # проверяем, что почта не изменилась
        response_data_after_updating = use_data_actions.get_user_data(logged_user_access_token) \
            .json()
        assert response_data_after_updating['user']['email'] \
               == response_data_before_updating['user']['email']


