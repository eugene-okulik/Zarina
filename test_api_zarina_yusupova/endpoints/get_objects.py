import requests
import allure

from endpoints.endpoint import Endpoint


class GetObjects(Endpoint):

    @allure.step('Run get all objects')
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.response

    @allure.step('Check that len of response is one')
    def check_that_len_of_response_is_one(self):
        assert len(self.json) == 1
