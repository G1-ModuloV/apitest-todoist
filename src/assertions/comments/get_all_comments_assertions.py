from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema


def assert_get_all_comments_of_task_success(response):
    schema = read_a_json("comments_of_task_schema.json")
    assert_schema(response, schema)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'

def assert_get_all_comments_of_project_success(response):
    schema = read_a_json("comments_of_project_schema.json")
    assert_schema(response, schema)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'

def assert_get_all_comments_bad_request(response):
    assert response.status_code == 400

def assert_get_all_comments_not_found(response):
    assert response.status_code == 404

def assert_get_all_comments_unauthorized(response):
    assert response.status_code == 401
