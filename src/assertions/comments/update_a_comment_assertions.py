import json
from src.resources.payloads.update_comment_data import data_comment_update


def assert_update_comment_success(response):
    assert response.status_code == 200


def assert_updated_comment_values_success(response):
    json_response = response.json()
    assert_update_comment_success(response)
    assert json_response['content'] == data_comment_update['content']

def assert_update_comment_unauthorized(response):
    assert response.status_code == 401
