import requests as r
import allure

class RegistrationUser:

    def __init__(self, url, payload):
        self.url = url
        self.payload = payload

    @allure.step('Вызов API-метода регистрации пользователя')
    def registration_user(self):
        response = r.post(self.url, data=self.payload)
        return response.status_code, response.json()