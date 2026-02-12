import allure
from project_api_memes.data import data1
from project_api_memes.data import data_aus


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    response = None
    json = None
    headers = {'Authorization': 'UkzafrVWZKgXRXN'}

    @allure.step('Check status code')
    def check_status_code(self, code):
        assert self.response.status_code == code

    @allure.step('Check json')
    def check_json(self):
        assert len(self.json) > 0

    @allure.step('Check response id')
    def check_id(self, expected_id):
        assert self.json['id'] == expected_id, \
            f"Expected id={expected_id}, got {self.json['id']}"

    @allure.step('Check response body')
    def check_response_body(self, expected_payload, expected_id=None):
        if expected_id:
            assert int(self.json['id']) == expected_id
        assert self.json['text'] == expected_payload['text']
        assert self.json['url'] == expected_payload['url']
        assert self.json['tags'] == expected_payload['tags']
        assert self.json['info'] == expected_payload['info']

    @allure.step('Check response name aus')
    def check_name(self):
        assert self.json['user'] == data_aus['name']


