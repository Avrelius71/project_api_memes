from project_api_memes.method.endpoint import Endpoint
import requests
import allure


class GetAllMemes(Endpoint):

    @allure.step('Get all memes')
    def get_all_memes(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        try:
            self.json = self.response.json()
        except Exception:
            self.json = None
        return self.response
