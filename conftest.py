import pytest
from urls import URLs
from helpers import generate_user_data
from methods.registration_methods import RegistrationUser
from methods.create_listing_methods import CreateListing
from methods.delete_listing_methods import DeleteListing



@pytest.fixture()
def create_user():

    test_data = generate_user_data()
    user = RegistrationUser(URLs.REGISTRATION_URL, test_data)
    _, response = user.registration_user()
    
    yield response["access_token"]["access_token"]



@pytest.fixture()
def create_listing(create_user):
    
    token = create_user

    create = create = CreateListing(URLs.CREATE_LISTING_URL, token)
    _, response_body = create.create_listing()

    yield token, response_body["id"]



@pytest.fixture()
def create_and_delete_offer(create_user, create_listing):

    token = create_user
    token, response_body = create_listing
    
    yield token, response_body

    delete = DeleteListing(URLs.DELETE_LISTING_URL, token)
    delete.delete_listing(response_body)
