import allure
import requests as r
from requests_toolbelt import MultipartEncoder



class UpdateOffer:

    def __init__(self, url, token):
        self.url = url
        self.payload = self.payload = MultipartEncoder(fields= {
            "name": "",
            "category": 'Авто',
            "condition": "Новый",
            "city": "Москва",
            "description": "",
            "price": "50000"
        })
        self.token = token


    @allure.step('Вызов API-метода обновления объявления')
    def update_offer(self, id):

        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': self.payload.content_type  
        }

        response = r.patch(self.url+str(id), data=self.payload, headers=headers)

        return response.status_code, response.json()
    