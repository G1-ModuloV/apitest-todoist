
def assert_delete_a_comment_success(response):
    assert response.status_code == 204

def assert_delete_a_comment_unauthorized(response):
    assert response.status_code == 401