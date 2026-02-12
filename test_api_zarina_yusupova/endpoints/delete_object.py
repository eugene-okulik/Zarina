import requests
import allure

from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Delete object by id")
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        return self.response

    @allure.step("Check that status 200")
    def check_status_code_is_200(self):
        self.check_that_status_is_200()
