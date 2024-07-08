

def assert_status_code(response, expected_code):
    assert response.status_code == expected_code


def assert_content_type(response, expected_content_type):
    assert response.headers['Content-Type'] == expected_content_type


def assert_json_contains(response, key):
    assert key in response.json()
