from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema


def assert_create_task_successful(response):
    assert response.status_code == 200
    assert response.json()['id'] is not None


def assert_create_a_task_json(response):
    schema = read_a_json("create_a_task_schema.json")
    assert_schema(response, schema)
    assert_create_task_successful(response)
    assert response.headers['Content-Type'] == 'application/json'


def assert_create_task_bad_request(response):
    assert response.status_code == 400


def assert_create_task_unauthorized(response):
    assert response.status_code == 401
