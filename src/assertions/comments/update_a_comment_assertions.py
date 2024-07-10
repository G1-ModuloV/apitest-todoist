from src.resources.payloads.update_comment_data import data_comment_update
from src.assertions.common_assertions import assert_empty_body
from src.todoist_api.response_content_type import ResponseContentType


def assert_update_comment_success(response):
    assert response.status_code == 200


def assert_updated_comment_values_success(response):
    json_response = response.json()
    assert_update_comment_success(response)
    assert json_response['content'] == data_comment_update['content']

def assert_update_comment_unauthorized(response):
    assert_empty_body(response, 401, ResponseContentType.TEXT_PLAIN.value, b'Forbidden')
