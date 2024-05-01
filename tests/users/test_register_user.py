import allure
import pytest

from constants.response_error_messages import ResponseErrorMessages
from helper_functions.users.register_user import RegisterUser


class TestRegisterUser:

    @allure.title('Регистрация пользователя успешна, если переданы допустимые логин, пароль и имя')
    def test_register_courier_with_all_fields_filled_success(self):
        register_courier = RegisterUser()
        payload = register_courier.get_register_payload()
        response = register_courier.send_register_user_request(payload)
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert response.json()['success'] == True
        assert response.json()['user']['email'] == payload['email']
        assert response.json()['user']['name'] == payload['name']
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()

    @allure.title(
        'Регистрация пользователя. Если переданы данные существующего пользователя, то регистрация неуспешна'
    )
    def test_register_user_with_existing_email_failure(self):
        register_user = RegisterUser()
        payload = register_user.get_register_payload()
        register_user.send_register_user_request(payload)
        response = register_user.send_register_user_request(payload)
        assert response.status_code == 403
        assert response.reason == 'Forbidden'
        assert response.json()['message'] == ResponseErrorMessages.USER_ALREADY_EXISTS

    @allure.title('Регистрация пользователя неуспешна, если переданы данные не все обязательные параметры. Тест для '
                  'отсутствующегоп поля {missed_payload_field}')
    @pytest.mark.parametrize(
        'missed_payload_field',
        [
            'name',
            'email',
            'password'
        ]
    )
    def test_register_user_with_with_not_all_required_params_fail(self, missed_payload_field):
        register_courier = RegisterUser()
        payload = register_courier.get_register_payload()
        payload.pop(missed_payload_field)
        response = register_courier.send_register_user_request(payload)
        assert response.status_code == 403
        assert response.reason == 'Forbidden'
        assert response.json()['message'] == ResponseErrorMessages.NOT_ENOUGH_DATA_TO_REGISTER

