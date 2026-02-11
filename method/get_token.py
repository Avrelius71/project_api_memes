from project_api_memes.method.endpoint import Endpoint
import requests
import allure


class GetToken(Endpoint):

    @allure.step('Get token')
    def get_token(self, token):
        self.response = requests.get(f'{self.url}/authorize/{token}')
        try:
            self.json = self.response.json()
        except Exception:
            self.json = None
        return self.response
