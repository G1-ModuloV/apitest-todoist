import pytest
from src.utils.project import get_a_project, post_a_project_with_id,get_a_project_with_invalid_url
from src.assertions.projects.get_a_project_assertions import (
    assert_get_a_project_code_200,
    assert_get_a_project_json,
    assert_get_a_project_code_401,
    assert_get_a_project_code_404,
    assert_get_a_project_code_400
)


@pytest.mark.smoke
@pytest.mark.regression
# TD-9 Verificar respuesta exitosa con un ID de proyecto válido
def test_get_a_project_successful_response(valid_token, setup_create_project, valid_project_id):
    _, valid_project_id = setup_create_project("valid_name")
    response = get_a_project(valid_token, valid_project_id)
    assert_get_a_project_code_200(response)

@pytest.mark.regression
# TD-9 Verificar que el objeto JSON en la respuesta contenga los campos esperados
def test_get_a_project_valid_json(valid_token, setup_create_project, valid_project_id):
    _, valid_project_id = setup_create_project("valid_name")
    response = get_a_project(valid_token, valid_project_id)
    assert_get_a_project_json(response, valid_project_id)


@pytest.mark.regression
# TD-9 Verificar la respuesta con un ID de proyecto inválido
def test_get_a_project_invalid_id(invalid_project_id, valid_token):
    response = get_a_project(valid_token, invalid_project_id)
    assert_get_a_project_code_400(response)


@pytest.mark.regression
# TD-9 Verificar la respuesta cuando falta el token de autorización
def test_get_a_project_no_token(valid_project_id, no_token, setup_create_project):
    _, valid_project_id = setup_create_project("valid_name")
    response = get_a_project(no_token, valid_project_id)
    assert_get_a_project_code_401(response)


@pytest.mark.regression
# TD-9 Verificar la respuesta con un token de autorización incorrecto
def test_get_a_project_invalid_token(valid_project_id, invalid_token):
    response = get_a_project(invalid_token, valid_project_id)
    assert_get_a_project_code_401(response)


@pytest.mark.regression
# TD-9 Verificar la respuesta para un ID de proyecto inexistente
def test_get_a_project_nonexistent_id(nonexistent_project_id, valid_token):
    response = get_a_project(valid_token, nonexistent_project_id)
    assert_get_a_project_code_404(response)


@pytest.mark.regression
# TD-9 Verificar la respuesta con un formato de URL incorrecto
def test_get_a_project_invalid_url_format(valid_project_id, valid_token, setup_create_project):
    _, valid_project_id = setup_create_project("valid_name")
    response = get_a_project_with_invalid_url(valid_project_id, valid_token)
    assert_get_a_project_code_404(response)


@pytest.mark.regression
# TD-9 Verificar la respuesta cuando el ID de proyecto es nulo
def test_get_a_project_null_id(valid_token):
    response = get_a_project(valid_token, None)
    assert_get_a_project_code_400(response)


@pytest.mark.regression
# TD-9 Verificar la respuesta con un ID de proyecto en formato incorrecto (alfanumérico)
def test_get_a_project_alphanumeric_id(alphanumeric_project_id, valid_token):
    response = get_a_project(valid_token, alphanumeric_project_id)
    assert_get_a_project_code_400(response)


@pytest.mark.regression
# TD-9 Verificar la respuesta con un método HTTP incorrecto (POST en lugar de GET)
def test_get_a_project_post_method(valid_project_id, valid_token, setup_create_project):
    _, valid_project_id = setup_create_project("valid_name")
    response = post_a_project_with_id(valid_token, valid_project_id)
    assert_get_a_project_code_400(response)


@pytest.mark.regression
# TD-9 Verificar la respuesta cuando la URL del endpoint está mal escrita
def test_get_a_project_invalid_endpoint(valid_project_id, valid_token, setup_create_project):
    _, valid_project_id = setup_create_project("valid_name")
    response = get_a_project_with_invalid_url(valid_project_id, valid_token)
    assert_get_a_project_code_404(response)
