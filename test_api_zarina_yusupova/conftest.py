import pytest
from endpoints.get_objects import GetObjects
from endpoints.create_object import CreateObject
from endpoints.get_object_by_id import GetOneObject
from endpoints.delete_object import DeleteObject
from endpoints.update_object import UpdateObject
from endpoints.patch_object import PatchObject


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


@pytest.fixture()
def get_objects_endpoint(for_every_test, for_all_tests):
    return GetObjects()


@pytest.fixture()
def create_object_endpoint(for_every_test):
    return CreateObject()


@pytest.fixture()
def delete_object_endpoint(for_every_test):
    return DeleteObject()


@pytest.fixture()
def object_id_f(create_object_endpoint, delete_object_endpoint):
    payload = {"name": "Second object", "data": {"color": "red", "size": "big"}}
    create_object_endpoint.create_new_object(payload)
    yield create_object_endpoint.object_id
    delete_object_endpoint.delete_object(create_object_endpoint.object_id)


@pytest.fixture()
def get_object_by_id_endpoint(for_every_test):
    return GetOneObject()


@pytest.fixture()
def update_object_endpoint(for_every_test):
    return UpdateObject()


@pytest.fixture()
def patch_object_endpoint(for_every_test):
    return PatchObject()
