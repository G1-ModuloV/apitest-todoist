def assert_delete_task_successful(response):
    assert response.status_code == 204


def assert_delete_task_bad_request(response):
    assert response.status_code == 400


def assert_delete_task_not_found(response):
    assert response.status_code == 404


def assert_delete_task_unauthorized(response):
    assert response.status_code == 401
