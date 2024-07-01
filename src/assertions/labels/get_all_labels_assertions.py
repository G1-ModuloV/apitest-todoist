from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema


def assert_get_all_labels_case_one(response):
    schema = read_a_json("labels_schema.json")
    assert_schema(response, schema)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'


def assert_get_all_labels_forbidden(response):
    assert response.status_code == 401
    assert response.headers['Content-Type'] == 'text/plain; charset=utf-8'
    assert response.content == b'Forbidden'


def assert_get_all_labels_invalid_format(response):
    assert response.status_code == 403
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json()["error"] == 'Invalid format for Authentication header'
