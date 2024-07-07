import pytest
from src.utils.task import get_a_task
from src.assertions.tasks.get_an_active_task_assertions import (
    assert_get_a_task_successful,
    assert_get_a_task_json,
    assert_get_a_task_unauthorized,
    assert_get_a_task_bad_request,
    assert_get_a_task_not_found)


@pytest.mark.smoke
@pytest.mark.regression
# TD-20 Verificar que se pueda recuperar una tarea activa con un token de acceso válido
def test_get_an_active_task(valid_task_id, valid_token):
    response = get_a_task(valid_task_id, valid_token)
    assert_get_a_task_successful(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-20 Verificar que se reciba el contenido de una tarea activa
def test_get_an_active_task_schema(valid_task_id, valid_token):
    response = get_a_task(valid_task_id, valid_token)
    assert_get_a_task_json(response)


@pytest.mark.regression
# TD-20 Verificar que no se pueda recuperar una tarea activa con un token de acceso inválido
def test_get_an_active_task_invalid_token(valid_task_id, invalid_token):
    response = get_a_task(valid_task_id, invalid_token)
    assert_get_a_task_unauthorized(response)


@pytest.mark.regression
# TD-20 Verificar que no se pueda recuperar una tarea sin token de autenticación
def test_get_an_active_task_no_token(valid_task_id, no_token):
    response = get_a_task(valid_task_id, no_token)
    assert_get_a_task_unauthorized(response)


@pytest.mark.regression
# TD-20 Verificar que se reciba un error al intentar recuperar una tarea con un ID no numérico (letras en el ID)
def test_get_a_task_non_numeric_id(invalid_task_id, valid_token):
    response = get_a_task(invalid_task_id, valid_token)
    assert_get_a_task_bad_request(response)


@pytest.mark.regression
# TD-20 Verificar que no se pueda recuperar una tarea con un ID inexistente
def test_get_a_task_non_existent_id(non_existent_task_id, valid_token):
    response = get_a_task(non_existent_task_id, valid_token)
    assert_get_a_task_not_found(response)


@pytest.mark.regression
# TD-20 Verificar que se reciba un error al intentar recuperar una tarea con un ID que ha sido borrado
def test_get_a_task_deleted_id(deleted_task_id, valid_token):
    response = get_a_task(deleted_task_id, valid_token)
    assert_get_a_task_not_found(response)


@pytest.mark.regression
# TD-20 Verificar que se reciba un error al intentar recuperar una tarea sin especificar un ID nulo/vacio
def test_get_a_task_null_id(null_task_id, valid_token):
    response = get_a_task(null_task_id, valid_token)
    assert_get_a_task_bad_request(response)
