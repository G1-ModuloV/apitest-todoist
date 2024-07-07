from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema

def assert_get_all_tasks_success(response):
    schema = read_a_json("schema_get_tasks.json")
    assert_schema(response, schema)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'

def assert_get_all_tasks_of_project_success(response):
    schema = read_a_json("schema_get_tasks.json")
    assert_schema(response, schema)
    assert response.status_code == 200
    #assert_get_tasks_success(response)
    assert response.headers['Content-Type'] == 'application/json'

def assert_get_all_tasks_of_seccion_success(response):
    schema = read_a_json("schema_get_tasks.json")
    assert_schema(response, schema)
    assert response.status_code == 200
    #assert_get_tasks_success(response)
    assert response.headers['Content-Type'] == 'application/json'

def assert_get_all_tasks_bad_request(response):
    assert response.status_code == 400

def assert_get_all_tasks_unauthorized(response):
    assert response.status_code == 401



