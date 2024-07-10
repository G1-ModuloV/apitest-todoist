from src.assertions.schema_assertion import assert_schema
from src.todoist_api.response_content_type import ResponseContentType
from src.assertions.common_assertions import assert_empty_body
from src.utils.json_reader import read_a_json


def assert_create_a_comment_success(response):
    schema = read_a_json("comment_create_schema.json")
    assert_schema(response, schema)
    assert response.status_code == 200

def assert_create_a_comment_unauthorized(response):
    assert_empty_body(response, 401, ResponseContentType.TEXT_PLAIN.value, b'Forbidden')
