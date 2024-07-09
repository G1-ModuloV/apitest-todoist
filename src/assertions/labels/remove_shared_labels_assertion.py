

def assert_post_remove_a_shared_label(response):
    assert response.status_code == 204

def assert_post_remove_a_shared_label_invalid_token (response):
    assert response.status_code == 401

def assert_get_remove_a_shared_label (response):
    assert response.status_code == 403


def assert_remove_a_shared_label_invalid_body (response):
    assert response.status_code == 400