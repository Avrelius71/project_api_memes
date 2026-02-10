from project_api_memes.method.endpoint import Endpoint
import requests
import allure


class PutMemes(Endpoint):

    @allure.step('update memes')
    def put_memes(self, id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/meme/{id}', json=payload, headers=headers)
        try:
            self.json = self.response.json()
        except Exception:
            self.json = None
        return self.response
