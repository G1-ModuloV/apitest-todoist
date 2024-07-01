from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema


def assert_get_a_task_successful(response):
    assert response.status_code == 200


def assert_get_a_task_json(response):
    schema = read_a_json("a_task_schema.json")
    assert_schema(response, schema)
    assert_get_a_task_successful(response)
    assert response.headers['Content-Type'] == 'application/json'


def assert_get_a_task_bad_request(response):
    assert response.status_code == 400


def assert_get_a_task_unauthorized(response):
    assert response.status_code == 401


def assert_get_a_task_not_found(response):
    assert response.status_code == 404
