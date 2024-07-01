import pytest
import requests
from src.login import get_token
from src.utils.task import get_a_task
from src.assertions.tasks.get_an_active_task_assertions import (
    assert_get_a_task_successful,
    assert_get_a_task_json,
    assert_get_a_task_unauthorized,
    assert_get_a_task_bad_request,
    assert_get_a_task_not_found)
from config import BASE_URI


@pytest.mark.smoke
# Verificar que se pueda recuperar una tarea activa con un token de acceso válido
def test_get_an_active_task():
    response = get_a_task("8160389085", get_token())
    assert_get_a_task_successful(response)


@pytest.mark.smoke
# Verificar que se reciba el contenido de una tarea activa
def test_get_an_active_task_schema():
    response = get_a_task("8160389085", get_token())
    assert_get_a_task_json(response)


@pytest.mark.functional
# Verificar que no se pueda recuperar una tarea activa con un token de acceso inválido
def test_get_an_active_task_invalid_token():
    invalid_token = "invalid_token"
    response = get_a_task("8160389085", invalid_token)
    assert_get_a_task_unauthorized(response)


@pytest.mark.functional
# Verificar que no se pueda recuperar una tarea sin token de autenticación
def test_get_an_active_task_no_token():
    url = f"{BASE_URI}/rest/v2/tasks/8160389085"
    response = requests.get(url)
    assert_get_a_task_unauthorized(response)


@pytest.mark.functional
# Verificar que se reciba un error al intentar recuperar una tarea con un ID no numérico (letras en el ID)
def test_get_a_task_non_numeric_id():
    response = get_a_task("invalid_id", get_token())
    assert_get_a_task_bad_request(response)


@pytest.mark.functional
# Verificar que no se pueda recuperar una tarea con un ID inexistente
def test_get_a_task_non_existent_id():
    response = get_a_task("9999999999", get_token())
    assert_get_a_task_not_found(response)


@pytest.mark.functional
# Verificar que se reciba un error al intentar recuperar una tarea con un ID que ha sido borrado
def test_get_a_task_deleted_id():
    response = get_a_task("8164612172", get_token())
    assert_get_a_task_not_found(response)


@pytest.mark.functional
# Verificar que se reciba un error al intentar recuperar una tarea sin especificar un ID nulo/vacio
def test_get_a_task_null_id():
    response = get_a_task(None, get_token())
    assert_get_a_task_bad_request(response)
