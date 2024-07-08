from src.assertions.common_assertions import assert_empty_body


def assert_delete_a_label_successfully(response):
    assert_empty_body(response, 204, 'text/html; charset=utf-8', b'')


def assert_delete_a_label_forbidden(response):
    assert_empty_body(response, 401, 'text/plain; charset=utf-8', b'Forbidden')
