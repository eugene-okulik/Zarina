import pytest

TEST_DATA = [
    {"name": "Second object", "data": {"color": "red", "size": "big"}},
    {"name": "Third object", "data": {"color": "red", "size": "big"}},
    {"name": "Fourth object", "data": {"color": "red", "size": "big"}},
]


def test_receive_objects(get_objects_endpoint):
    get_objects_endpoint.get_all_objects()
    get_objects_endpoint.check_that_len_of_response_is_one()


@pytest.mark.parametrize('data', TEST_DATA)
def test_add_object(create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_that_name_of_object_is_correct(data)
    create_object_endpoint.check_that_data_of_object_is_correct(data)


def test_receive_object_by_id(get_object_by_id_endpoint, object_id_f):
    get_object_by_id_endpoint.get_one_object(object_id_f)
    get_object_by_id_endpoint.check_that_object_id_is_correct(object_id_f)


def test_put_object(update_object_endpoint, object_id_f):
    payload = {"name": "Thirddd object", "data": {"color": "blue", "size": "small"}}
    update_object_endpoint.make_changes_in_object(object_id_f, payload)
    update_object_endpoint.check_that_name_of_object_is_correct(payload)
    update_object_endpoint.check_that_data_of_object_is_correct(payload)


def test_patch_object(patch_object_endpoint, object_id_f):
    new_name = {"name": "Fifth object"}
    old_data = {"data": {"color": "red", "size": "big"}}
    patch_object_endpoint.make_changes_in_object(object_id_f, new_name)
    patch_object_endpoint.check_that_name_of_object_is_correct(new_name)
    patch_object_endpoint.check_that_data_of_object_is_correct(old_data)


def test_delete_object(delete_object_endpoint, object_id_f):
    delete_object_endpoint.delete_object(object_id_f)
    delete_object_endpoint.check_that_status_is_200()
