from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema

def assert_post_create_a_personal_label_name_valid(response):
    schema = read_a_json("label_schema.json")
    assert_schema(response, schema)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'