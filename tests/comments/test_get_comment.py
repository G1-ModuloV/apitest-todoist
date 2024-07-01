
from src.login import get_token
import pytest
from src.utils.comment import get_a_comment
from src.assertions.comments.get_a_comment_assertion import assert_get_a_comment_success, \
    assert_get_a_comment_code_400, assert_get_a_comment_code_401

#Verificar que el request retorna un codigo de error usando un codigo de autenticación invalido
def test_get_a_comment_token_invalid(valid_comment_id, invalid_token):
    response = get_a_comment(valid_comment_id, invalid_token)
    assert_get_a_comment_code_401(response)

#Verificar que el retorna un codigo de error usando un codigo de autenticacion nulo/vacio
def test_get_a_comment_token_nul(valid_comment_id, no_token):
    response = get_a_comment(valid_comment_id, no_token)
    assert_get_a_comment_code_401(response)

#Verificar que el request retorna un comentario especifico usando el id valido del comentario
def test_a_comment(valid_token, valid_comment_id):
    response = get_a_comment(valid_token, valid_comment_id)
    assert_get_a_comment_success(response, valid_comment_id)

#Verificar que el request retorna un codigo de error usando un id de comentario invalido
def test_get_a_comment_invalid_id(valid_token, invalid_comment_id):
    response = get_a_comment(valid_token, invalid_comment_id)
    assert_get_a_comment_code_400(response)

#Verificar que el request retorna un codigo de error usando el nulo/vacio del comentario
def test_get_a_comment_null_id(valid_token):
    response = get_a_comment(valid_token, None)
    assert_get_a_comment_code_400(response)