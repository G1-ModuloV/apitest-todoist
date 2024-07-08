import pytest
import json
from src.utils.comment import delete_a_comment
from src.assertions.comments.delete_a_comment_assertion import assert_delete_a_comment_success

@pytest.mark.smoke
# TD-11 Verificar que se elimine un comentario con id valido
def test_delete_comment(setup_and_teardown_delete_comment, valid_token):
    comment_id = setup_and_teardown_delete_comment
    response = delete_a_comment(valid_token, comment_id)
    assert_delete_a_comment_success(response)