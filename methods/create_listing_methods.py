import allure
import requests as r
from requests_toolbelt import MultipartEncoder


class CreateListing:

    def __init__(self, url, token):
        self.url = url
        self.payload = self.payload = MultipartEncoder(fields= {
            "name": "",
            "category": 'Авто',
            "condition": "Новый",
            "city": "Москва",
            "description": "",
            "price": "0"
        })
        self.token = token





    @allure.step('Вызов API-метода создания объявления')
    def create_listing(self):
        
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': self.payload.content_type  
        }

        response = r.post(self.url, data=self.payload, headers=headers)
        
        return response.status_code, response.json()
