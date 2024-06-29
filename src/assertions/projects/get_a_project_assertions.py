from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema

def assert_get_a_project_code_200(response):
    assert response.status_code == 200

def assert_get_a_project_json(response):
    schema = read_a_json("project_schema.json")
    assert_schema(response, schema)
    assert response.headers['Content-Type'] == 'application/json'
    response_json = response.json()
    expected_project_id = "2335308589"
    assert response_json['id'] == expected_project_id, f"Expected project ID {expected_project_id}, but got {response_json['id']}"
