def assert_empty_body(response, status_code, content_type, content=b''):
    assert response.status_code == status_code
    assert response.headers['Content-Type'] == content_type
    assert response.content == content
