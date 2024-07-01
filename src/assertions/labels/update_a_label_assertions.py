from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema


def assert_update_a_label_case_one(response, label_data):
    schema = read_a_json("label_schema.json")
    assert_schema(response, schema)
    response_data = response.json()
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data["name"] == label_data["name"]
