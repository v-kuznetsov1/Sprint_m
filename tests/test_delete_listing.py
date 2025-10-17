import allure
from urls import URLs
from data import TestData
from methods.delete_listing_methods import DeleteListing


class TestDeleteListing:

    @allure.step('Проверка возможности удаления объявления')
    def test_delete_listing(self, create_listing):

        token, offer_id = create_listing

        delete = DeleteListing(URLs.DELETE_LISTING_URL, token)
        status_code, response_body = delete.delete_listing(offer_id)

        with allure.step('Провека кода и тела ответа'):
            assert status_code == 200
            assert response_body["message"] == TestData.DELETE_MESSAGE
            