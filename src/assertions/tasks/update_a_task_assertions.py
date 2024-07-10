from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema

def assert_post_update_a_task_case_one(response):
    schema = read_a_json("task_schema.json")
    assert_schema(response, schema)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
