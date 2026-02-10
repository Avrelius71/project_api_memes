from project_api_memes.method.endpoint import Endpoint
import requests
import allure


class GetOneMemes(Endpoint):

    @allure.step('Get one memes')
    def get_one_memes(self, id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme/{id}', headers=headers)
        try:
            self.json = self.response.json()
        except Exception:
            self.json = None
        return self.response
