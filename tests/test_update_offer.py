import allure
from urls import URLs
from methods.update_offer_methods import UpdateOffer
from methods.registration_methods import RegistrationUser
from helpers import generate_user_data
from data import TestData


class TestUpdateOffer:

    @allure.title('Проверка возможности редактирования объявления')
    def test_update_offer_successfully(self, create_and_delete_offer):

        token, offer_id = create_and_delete_offer

        update = UpdateOffer(URLs.UPDATE_OFFER_URL, token)
        status_code, response_body = update.update_offer(offer_id)

        with allure.step('Проверка кода и тела ответа'):
            assert status_code == 200
            assert list(response_body) == TestData.UPDATE_OFFER_RESPONSE


    
    @allure.title('Проверка возможности редактиварования объявления другим пользователем')
    def test_update_offer_other_user(self, create_and_delete_offer):

        with allure.step('Создание пользователя, которому не принадлежит объявление'):
            test_data = generate_user_data()
            registration = RegistrationUser(URLs.REGISTRATION_URL, test_data)
            _, response = registration.registration_user()
            token_other_user = response["access_token"]["access_token"]
        
        _, offer_id = create_and_delete_offer
  
        update = UpdateOffer(URLs.UPDATE_OFFER_URL, token_other_user)
        status_code, response_body = update.update_offer(offer_id)

        with allure.step('Проверка кода и тела ответа'):
            assert status_code == 401
            assert response_body["message"] == TestData.NO_UPDATING_RIGHTS
