from src.assertions.common_assertions import assert_empty_body
from src.todoist_api.response_content_type import ResponseContentType


def assert_rename_share_labels_forbidden(response):
    assert_empty_body(response, 401, ResponseContentType.TEXT_PLAIN.value, b'Forbidden')


def assert_rename_share_labels_new_name_required(response):
    assert_empty_body(response, 400, ResponseContentType.TEXT_PLAIN.value, b'new_name required')


def assert_rename_share_labels_successfully(response):
    assert_empty_body(response, 204, ResponseContentType.TEXT_HTML.value)


def assert_a_share_label_exists(label, share_labels):
    assert str(label) in share_labels


def assert_there_is_no_a_share_label(label, share_labels):
    assert str(label) not in share_labels
