import requests
import allure

from endpoints.endpoint import Endpoint


class GetOneObject(Endpoint):
    @allure.step("Run get object by id")
    def get_one_object(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()
        return self.response

    @allure.step("Check that object id is correct")
    def check_that_object_id_is_correct(self, object_id):
        assert self.json["id"] == object_id
