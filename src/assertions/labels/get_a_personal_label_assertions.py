from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema


def assert_get_personal_label_valid_case(response):
    assert response.status_code == 200


def assert_get_personal_label_case_invalid_token(response):
    assert response.status_code == 401

def assert_get_personal_label_case_correct_date(response, project_id):
    schema = read_a_json("personal_label_schema.json")
    assert_schema(response, schema)
    assert response.headers['Content-Type'] == 'application/json'
    response_json = response.json()
    assert response_json['id'] == project_id

def assert_get_personal_label_case_not_found(response):
    assert response.status_code == 404



