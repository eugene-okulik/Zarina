import requests


def all_posts():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    print(response)


def one_post():
    response = requests.get('http://objapi.course.qa-practice.com/object/1').json()
    print(response)
    assert response["id"] == 1


def post_a_post():
    body = {
        "name": "Second object",
        "data": {"color": "red", "size": "big"}
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers).json()
    assert response["name"] == "Second object"


def new_post():
    body = {
        "name": "Second object",
        "data": {"color": "red", "size": "big"}
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers)
    return response.json()["id"]


def clear_a_post(post_id):
    requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")


def put_a_post():
    post_id = new_post()
    body = {
        "name": "Thirddd object",
        "data": {"color": "blue", "size": "small"}
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(f"http://objapi.course.qa-practice.com/object/{post_id}", json=body, headers=headers).json()
    assert response["data"] == {"color": "blue", "size": "small"}
    clear_a_post(post_id)


def patch_a_post():
    post_id = new_post()
    body = {"name": "Fifth object"}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(f"http://objapi.course.qa-practice.com/object/{post_id}", json=body, headers=headers)
    assert response.json()["data"] == {"color": "red", "size": "big"}
    clear_a_post(post_id)


def delete_a_post():
    post_id = new_post()
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")
    print(response.status_code)
