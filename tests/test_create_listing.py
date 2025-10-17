import allure
from urls import URLs
from methods.create_listing_methods import CreateListing
from methods.delete_listing_methods import DeleteListing
from data import TestData


class TestCreateListing:

    @allure.title('Проверка создания объявления через API')
    def test_create_listing(self, create_user):
        
        token = create_user

        listing = CreateListing(
            URLs.CREATE_LISTING_URL,
            token
            )
        
        status_code, response_body = listing.create_listing()
        
        with allure.step('Проверка тела ответа и всех ожидаемых ключей'):
            assert status_code == 201
            assert list(response_body) == TestData.CREATE_LISTING_RESPONSE

        with allure.step('Удаление тестового объявления'):
            delete = DeleteListing(URLs.DELETE_LISTING_URL, token)
            delete.delete_listing(response_body["id"])
