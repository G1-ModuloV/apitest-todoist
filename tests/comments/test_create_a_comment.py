import pytest
import json

from src.assertions.comments.create_a_comment_assertion import assert_create_a_comment_unauthorized
from src.utils.comment import get_a_comment, create_a_comment
from src.assertions.comments.get_a_comment_assertion import assert_get_a_comment_success
from src.resources.payloads.create_comment_data import comment_body


@pytest.mark.smoke
#TD-14 Verificar que el request retorna crea un comentario valido
def test_create_a_comment(valid_token, setup_and_teardown_create_comment):
    commentID = setup_and_teardown_create_comment
    response = get_a_comment(valid_token, commentID)
    assert_get_a_comment_success(response, commentID)

@pytest.mark.smoke
#TD-14 Verificar que el request retorna un codigo de error usando un codigo de autenticación invalido
def test_create_a_comment_invalid_token(invalid_token):
    # commentID = setup_and_teardown_create_comment
    response = create_a_comment(invalid_token, json.dumps(comment_body))
    assert_create_a_comment_unauthorized(response)