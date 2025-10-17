import allure
import requests as r

class DeleteListing:

    def __init__(self, url, token):
        self.url = url
        self.token = token 


    @allure.step('Вызов API-метода удаления объявления')
    def delete_listing(self, id):

        headers = {"Authorization": f'Bearer {self.token}'}
        
        response = r.delete(self.url+str(id), headers=headers)
        return response.status_code, response.json()
