from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema
from src.todoist_api.response_content_type import ResponseContentType
from src.assertions.common_assertions import assert_empty_body


def assert_get_all_comments_success(response):
    assert response.status_code == 200
    
def assert_get_all_comments_of_task_success(response):
    schema = read_a_json("comments_of_task_schema.json")
    assert_schema(response, schema)
    assert_get_all_comments_success(response)
    assert response.headers['Content-Type'] == ResponseContentType.APP_JSON.value

def assert_get_all_comments_of_project_success(response):
    schema = read_a_json("comments_of_project_schema.json")
    assert_schema(response, schema)
    assert_get_all_comments_success(response)
    assert response.headers['Content-Type'] == ResponseContentType.APP_JSON.value

def assert_get_all_comments_bad_request(response):
    assert_empty_body(response, 400, ResponseContentType.TEXT_PLAIN.value, b'Invalid argument value')

def assert_get_all_comments_not_found(response):
    assert response.status_code == 404

def assert_get_all_comments_unauthorized(response):
    # assert response.status_code == 401
    assert_empty_body(response, 401, ResponseContentType.TEXT_PLAIN.value, b'Forbidden')
