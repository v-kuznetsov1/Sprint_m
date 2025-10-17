import allure
from urls import URLs
from helpers import generate_user_data
from data import TestData
from methods.registration_methods import RegistrationUser

class TestRegistrationUser:

    @allure.title('Проверка успешной регистрации нового пользователя')
    def test_registration_user_successfully(self):

        test_data = generate_user_data()
        registration = RegistrationUser(
            URLs.REGISTRATION_URL, 
            test_data
            )
        status_code, response_body = registration.registration_user()

        with allure.step('Проверка кода ответа'):
            assert status_code == 201
        
        with allure.step('Проверка, что в теле возвращается email, переданный для регистрации'):  
            assert response_body['user']['email'] == test_data['email']
        
        with allure.step('Проверка, что в теле ответа вернулся токен для авторизации'):
            assert response_body['access_token']


    
    @allure.title('Проверка возможности зарегистрировать пользователя с существующим email')
    def test_registration_user_with_duplicate_email(self):

        test_data = generate_user_data()
        regisration = RegistrationUser(
            URLs.REGISTRATION_URL,
            test_data
        )
        regisration.registration_user()

        status_code, response_body = regisration.registration_user()

        with allure.step('Проверка статус кода и тела ответа'):
            assert status_code == 400
            assert response_body['message'] == TestData.EMAIL_ALREADY_USE
