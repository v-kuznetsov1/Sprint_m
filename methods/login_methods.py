import requests as r
import allure


class LoginUser:

    def __init__(self, url, user_data):
        self.url = url
        self.user_data = user_data

    
    @allure.step('Вызов API-метода авторизации пользователя')
    def authorization_user(self):
        
        response = r.post(self.url, self.user_data)
        return response.status_code, response.json()
