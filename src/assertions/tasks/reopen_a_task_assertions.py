from src.utils.task import get_a_task
def assert_reopen_task_no_content(response):
    assert response.status_code == 204

def assert_reopen_task_value_success(response, task_id, token):
    assert_reopen_task_no_content(response)
    get_response = get_a_task(task_id, token)
    task = get_response.json()
    assert task['is_completed'] is False

def assert_reopen_task_unauthorized(response):
    assert response.status_code == 401
