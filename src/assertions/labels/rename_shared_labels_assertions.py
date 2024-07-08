def assert_rename_share_labels_forbidden(response):
    assert_empty_body(response, 401, "text/plain; charset=utf-8", b'Forbidden')


def assert_rename_share_labels_new_name_required(response):
    assert_empty_body(response, 400, "text/plain; charset=utf-8", b'new_name required')


def assert_rename_share_labels_successfully(response):
    assert_empty_body(response, 204, 'text/html; charset=utf-8')


def assert_a_share_label_exists(label, share_labels):
    assert str(label) in share_labels


def assert_there_is_no_a_share_label(label, share_labels):
    assert str(label) not in share_labels


def assert_empty_body(response, status_code, content_type, content=b''):
    assert response.status_code == status_code
    assert response.headers['Content-Type'] == content_type
    assert response.content == content
