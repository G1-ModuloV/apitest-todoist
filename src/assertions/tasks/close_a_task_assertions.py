from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema


def assert_post_close_task_success(response):
    assert response.status_code == 204


def assert_post_close_task_bad_request(response):
    assert response.status_code == 400


def assert_post_close_task_unauthorized(response):
    assert response.status_code == 401


def assert_post_task_not_found(response):
    assert response.status_code == 404
