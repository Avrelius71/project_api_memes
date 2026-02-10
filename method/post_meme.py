from project_api_memes.method.endpoint import Endpoint
import requests
import allure


class PostMemes(Endpoint):
    @allure.step('create memes')
    def post_memes(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/meme', json=payload, headers=headers)
        try:
            self.json = self.response.json()
        except Exception:
            self.json = None
        return self.response
