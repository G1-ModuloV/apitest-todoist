from src.assertions.comments.create_a_comment_assertion import assert_create_a_comment_success
from src.login import get_token
import pytest
from src.utils.comment import create_a_comment
from src.resources.payloads.create_comment_data import comment_body


@pytest.mark.smoke
#Verificar que el request retorna crea un comentario valido
@pytest.mark.parametrize("payload", comment_body)
def test_create_a_comment(valid_token, payload):
    response = create_a_comment(valid_token, payload)
    assert_create_a_comment_success(response)