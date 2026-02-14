import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {"Content-Type": "application/json"}

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    def check_that_name_of_object_is_correct(self, data):
        assert self.json["name"] == data["name"]

    def check_that_data_of_object_is_correct(self, data):
        assert self.json["data"] == data["data"]
