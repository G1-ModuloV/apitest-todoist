from src.assertions.common_assertions import assert_empty_body
from src.todoist_api.response_content_type import ResponseContentType
from src.utils.comment import get_a_comment
from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema

def assert_get_a_comment_code_401(response):
    assert_empty_body(response, 400, ResponseContentType.TEXT_PLAIN.value, b'Invalid argument value')


def assert_get_a_comment_success(response, valid_comment_id):
    schema = read_a_json("comment_schema.json")
    assert_schema(response, schema)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    response_json = response.json()
    assert response_json['id'] == valid_comment_id

def assert_get_a_comment_code_400(response):
    assert response.status_code == 400
