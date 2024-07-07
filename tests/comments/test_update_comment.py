import json
import pytest
from src.utils.comment import update_a_comment
from src.resources.payloads.update_comment_data import data_comment_update
from src.assertions.comments.update_a_comment_assertions import (assert_updated_comment_values_success,
                                                                 assert_update_comment_unauthorized)

@pytest.mark.smoke
# TD-11 Verificar que se actualice un comentario con id valido mandando datos correctos
def test_update_comment(setup_teardown_update_comment, valid_token):
    comment_id = setup_teardown_update_comment
    response = update_a_comment(valid_token, comment_id, json.dumps(data_comment_update))
    assert_updated_comment_values_success(response)

@pytest.mark.smoke
# TD-11 Verificar que no se pueda actualizar un comentario dando un token de autorizacion invalido  SMOKE
def test_update_comment_with_invalid_token(setup_teardown_update_comment, invalid_token):
    comment_id = setup_teardown_update_comment
    response = update_a_comment(invalid_token, comment_id, json.dumps(data_comment_update))
    assert_update_comment_unauthorized(response)


@pytest.mark.smoke
# TD-11 Verificar que no se pueda actualizar un comentario sin dar un token de autorizacion  SMOKE
def test_update_comment_without_token(setup_teardown_update_comment, no_token):
    comment_id = setup_teardown_update_comment
    response = update_a_comment(no_token, comment_id, json.dumps(data_comment_update))
    assert_update_comment_unauthorized(response)
