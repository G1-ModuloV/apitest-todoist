def assert_delete_a_label_successfully(response):
    assert response.status_code == 204
    assert response.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert response.content == b''


def assert_delete_a_label_forbidden(response):
    assert response.status_code == 401
    assert response.headers['Content-Type'] == 'text/plain; charset=utf-8'
    assert response.content == b'Forbidden'
