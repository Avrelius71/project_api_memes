from project_api_memes.method.endpoint import Endpoint
import requests
import allure


class DeleteMemes(Endpoint):

    @allure.step('Delete memes')
    def delete_memes(self, id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/meme/{id}', headers=headers)
        try:
            self.json = self.response.json()
        except Exception:
            self.json = None
        return self.response
