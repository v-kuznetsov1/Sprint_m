import allure
from methods.login_methods import LoginUser
from methods.registration_methods import RegistrationUser
from urls import URLs
from helpers import generate_user_data
import requests as r


class TestLoginUser: 

    allure.title('Проверка авторизации пользователя через API')
    def test_login_user(self):
        
        user_data = generate_user_data()
        
        registration = RegistrationUser(URLs.REGISTRATION_URL, user_data)
        registration.registration_user()

        login_user = LoginUser(URLs.LOGIN_URL, user_data)
        status_code, response_body = login_user.authorization_user()
        
        with allure.step('Проверка статус кода ответа'):
            assert status_code == 201
        
        with allure.step('Проверка содержания ответа'):
            assert response_body['user']
            assert response_body['user']['email'] == user_data['email']
            assert response_body['token']['access_token']
        