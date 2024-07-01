from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema


def assert_get_a_project_code_200(response):
    assert response.status_code == 200

def assert_get_a_project_code_401(response):
    assert response.status_code == 401

def assert_get_a_project_code_404(response):
    assert response.status_code == 404

def assert_get_a_project_code_405(response):
    assert response.status_code == 405


def assert_get_a_project_json(response, project_id):
    schema = read_a_json("project_schema.json")
    assert_schema(response, schema)
    assert response.headers['Content-Type'] == 'application/json'
    response_json = response.json()
    assert response_json['id'] == project_id
