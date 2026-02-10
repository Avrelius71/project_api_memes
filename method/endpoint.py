import requests
import allure


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    response = None
    json = None
    headers = {'Authorization': 'MduMWg3KQZ5CuSA'}

# Не знаю как использовать!(

    # def aus(self):
    #     data = {'name': 'Artem'}
    #     self.response = requests.post(f'{self.url}/authorize', json=data)
    #     self.response = self.response.json()
    #     token = self.response['token']
    #     return token

    @allure.step('Check statu code')
    def check_status_code(self, code):
        assert self.response.status_code == code
