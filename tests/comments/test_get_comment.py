import pytest
from src.assertions.comments.create_a_comment_assertion import assert_create_a_comment_unauthorized
from src.utils.comment import get_a_comment
from src.assertions.comments.get_a_comment_assertion import assert_get_a_comment_success, assert_get_a_comment_code_401
from tests.comments.conftest import setup_and_teardown_create_comment


@pytest.mark.regression
#TD-16 Verificar que el request retorna un codigo de error usando un codigo de autenticación invalido
def test_get_a_comment_token_invalid(invalid_token, setup_and_teardown_create_comment):
    commentID = setup_and_teardown_create_comment
    response = get_a_comment(invalid_token, commentID)
    assert_create_a_comment_unauthorized(response)

@pytest.mark.regression
#TD-16 Verificar que el retorna un codigo de error usando un codigo de autenticacion nulo/vacio
def test_get_a_comment_token_nul(no_token, setup_and_teardown_create_comment):
    commentID = setup_and_teardown_create_comment
    response = get_a_comment(no_token, commentID)
    assert_create_a_comment_unauthorized(response)

@pytest.mark.smoke
@pytest.mark.regression
#TD-16 Verificar que el request retorna un comentario especifico usando el id valido del comentario
def test_a_comment(valid_token, setup_and_teardown_create_comment):
    commentID = setup_and_teardown_create_comment
    response = get_a_comment(valid_token, commentID)
    assert_get_a_comment_success(response, commentID)

@pytest.mark.regression
#TD-16 Verificar que el request retorna un codigo de error usando un id de comentario invalido
def test_get_a_comment_invalid_id(valid_token, invalid_comment_id):
    response = get_a_comment(valid_token, invalid_comment_id)
    assert_get_a_comment_code_401(response)

@pytest.mark.regression
#TD-16 Verificar que el request retorna un codigo de error usando el nulo/vacio del comentario
def test_get_a_comment_null_id(valid_token, null_comment_id):
    response = get_a_comment(valid_token, null_comment_id)
    assert_get_a_comment_code_401(response)