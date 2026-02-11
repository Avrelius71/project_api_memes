from project_api_memes.method.endpoint import Endpoint
import allure
import requests


class PostAus(Endpoint):
    @allure.step('Post Aus')
    def post_aus(self, payload):
        self.response = requests.post(f'{self.url}/authorize', json=payload)
        try:
            self.json = self.response.json()
        except Exception:
            self.json = None
        return self.response

