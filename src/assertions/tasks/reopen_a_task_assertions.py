from src.utils.task import get_a_task
from src.assertions.common_assertions import assert_empty_body
from src.todoist_api.response_content_type import ResponseContentType
def assert_reopen_task_no_content(response):
    assert_empty_body(response, 204, ResponseContentType.TEXT_HTML.value, b'')

def assert_reopen_task_value_success(response, task_id, token):
    assert_reopen_task_no_content(response)
    get_response = get_a_task(task_id, token)
    task = get_response.json()
    assert task['is_completed'] is False

def assert_reopen_task_unauthorized(response):
    assert_empty_body(response, 401, ResponseContentType.TEXT_PLAIN.value, b'Forbidden')
