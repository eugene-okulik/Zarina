import requests
import pytest
import allure


@pytest.fixture()
def new_object_id():
    body = {"name": "Second object", "data": {"color": "red", "size": "big"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers)
    object_id = response.json()["id"]
    yield object_id
    requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")


@pytest.fixture()
def for_every_test():
    print("before test")
    yield
    print(" after test")


@pytest.fixture(scope="session")
def for_all_tests():
    print("Start testing")
    yield
    print("Testing completed")


@allure.feature("objects")
@allure.story("Get objects")
@allure.title("Получение всех объектов")
def test_all_objects(for_every_test, for_all_tests):
    with allure.step("Run get all objects"):
        response = requests.get('http://objapi.course.qa-practice.com/object').json()
    with allure.step("Check that len(response) is 1"):
        assert len(response) == 1


@allure.feature("objects")
@allure.story("Get objects")
@allure.title("Получение объекта по id")
def test_one_object(new_object_id, for_every_test):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object_id}').json()
    assert response["id"] == new_object_id


@allure.feature("objects")
@allure.story("Post objects")
@allure.title("Добавление объекта")
@pytest.mark.parametrize(
    "bodies",
    [
        {"name": "Second object", "data": {"color": "red", "size": "big"}},
        {"name": "Third object", "data": {"color": "red", "size": "big"}},
        {"name": "Fourth object", "data": {"color": "red", "size": "big"}},
    ],
)
def test_add_object(for_every_test, bodies):
    headers = {"Content-Type": "application/json"}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=bodies, headers=headers).json()
    assert response["name"] == bodies["name"]
    assert response["data"] == bodies["data"]


@allure.feature("objects")
@allure.story("Put objects")
@allure.title("Изменение объекта")
@pytest.mark.critical
def test_put_object(new_object_id, for_every_test):
    body = {"name": "Thirddd object", "data": {"color": "blue", "size": "small"}}
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{new_object_id}", json=body, headers=headers
    )
    assert response.json()["data"] == {"color": "blue", "size": "small"}


@allure.feature("objects")
@allure.story("Put objects")
@allure.title("Изменение объекта")
@pytest.mark.medium
def test_patch_object(new_object_id, for_every_test):
    body = {"name": "Fifth object"}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{new_object_id}", json=body, headers=headers
    )
    assert response.json()["data"] == {"color": "red", "size": "big"}


@allure.feature("objects")
@allure.story("Delete objects")
@allure.title("Удаление объекта")
def test_delete_object(new_object_id, for_every_test):
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{new_object_id}")
    assert response.status_code == 200
