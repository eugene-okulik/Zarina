from locust import task, HttpUser
import random


class QaPractice(HttpUser):
    @task(1)
    def get_all_objects(self):
        self.client.get('/object')

    @task(3)
    def get_one_object(self):
        self.client.get(f'/object/{random.choice([1, 423, 426, 428, 477])}')

    @task(5)
    def add_object(self):
        headers = {"Content-Type": "application/json"}
        body = {"name": "Second object", "data": {"color": "red", "size": "big"}}
        self.client.post('/object', json=body, headers=headers)

    @task(2)
    def put_object(self):
        body = {"name": "Thirddd object", "data": {"color": "blue", "size": "small"}}
        headers = {"Content-Type": "application/json"}
        self.client.put('/object/1', json=body, headers=headers)

    @task(2)
    def patch_object(self):
        body = {"name": "Fifth object"}
        headers = {"Content-Type": "application/json"}
        self.client.patch('/object/1', json=body, headers=headers)

    @task(3)
    def delete_object(self):
        self.client.delete('/object/469')
