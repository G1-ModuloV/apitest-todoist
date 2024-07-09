from src.assertions.common_assertions import assert_empty_body
from src.todoist_api.response_content_type import ResponseContentType


def assert_delete_a_label_successfully(response):
    assert_empty_body(response, 204, ResponseContentType.TEXT_HTML.value, b'')


def assert_delete_a_label_forbidden(response):
    assert_empty_body(response, 401, ResponseContentType.TEXT_PLAIN.value, b'Forbidden')
