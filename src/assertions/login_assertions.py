
def assert_login_successfully(response, payload):
    assert response['full_name'] == payload["full_name"]
    assert response['email'] == payload["email"]
    assert response['token'] is not None
