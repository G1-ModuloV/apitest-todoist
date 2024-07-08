from src.assertions.schema_assertion import assert_schema
from src.utils.json_reader import read_a_json


def assert_delete_a_comment_success(response):
    #schema = read_a_json("comment_create_schema.json")
    #assert_schema(response, schema)
    assert response.status_code == 204

def assert_delete_a_comment_unauthorized(response):
    assert response.status_code == 401