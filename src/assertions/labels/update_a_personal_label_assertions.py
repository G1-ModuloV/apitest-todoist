from src.todoist_api.response_content_type import ResponseContentType
from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema
from src.assertions.common_assertions import assert_empty_body


def assert_update_a_label_case_one(response, label_data):
    schema = read_a_json("label_schema.json")
    assert_schema(response, schema)
    response_data = response.json()
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    for key in label_data.keys():
        assert response_data[key] == label_data[key]


def assert_update_a_label_name_already_exists(response):
    assert_bad_request(response, b'Label with this name already exists')


def assert_update_a_label_empty_payload(response):
    assert_bad_request(response, b'At least one of name, order, color or is_favorite fields should be set')


def assert_update_a_label_invalid_argument_value(response):
    assert_bad_request(response, b'Invalid argument value')


def assert_update_a_label_color_format_not_valid(response):
    assert_bad_request(response, b'Color format is not valid')


def assert_update_a_label_not_found(response):
    assert_empty_body(response, 404, ResponseContentType.TEXT_PLAIN.value, b'Label not found')


def assert_bad_request(response, content):
    assert_empty_body(response, 400, ResponseContentType.TEXT_PLAIN.value, content)
