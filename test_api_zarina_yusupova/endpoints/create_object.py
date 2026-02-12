import requests
import allure

from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    object_id = None

    @allure.step("Create new object")
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=payload, headers=headers)
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response

    @allure.step("Check that name and data of object are correct")
    def check_that_name_and_data_of_object_are_correct(self, data):
        assert self.json["name"] == data["name"]
        assert self.json["data"] == data["data"]
