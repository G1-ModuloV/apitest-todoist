import pytest
from src.utils.task import delete_task
from src.assertions.tasks.delete_a_task_assertions import (
    assert_delete_task_successful,
    assert_delete_task_unauthorized,
    assert_delete_task_bad_request, assert_delete_task_not_found
)


@pytest.mark.smoke
@pytest.mark.regression
# TD-21 Verificar que una tarea pueda ser eliminada usando su ID.
def test_delete_task_with_valid_id(setup_create_delete_task, valid_token):
    task_id = setup_create_delete_task
    response = delete_task(task_id, valid_token)
    assert_delete_task_successful(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-21 Verificar que no se pueda eliminar una tarea sin un token de autorización.
def test_delete_task_without_token(setup_create_delete_task, no_token):
    task_id = setup_create_delete_task
    response = delete_task(task_id, no_token)
    assert_delete_task_unauthorized(response)


@pytest.mark.regression
# TD-21 Verificar que no se pueda eliminar una tarea con un ID inválido.
def test_delete_task_with_invalid_id(invalid_task_id, valid_token):
    response = delete_task(invalid_task_id, valid_token)
    assert_delete_task_bad_request(response)


@pytest.mark.regression
# TD-21 Verificar que no se pueda eliminar una tarea con un ID no existente.
def test_delete_task_with_non_existent_id(non_existent_task_id, valid_token):
    response = delete_task(non_existent_task_id, valid_token)
    assert_delete_task_not_found(response)


@pytest.mark.regression
# TD-21 Verificar que no se pueda eliminar una tarea con un token de autorización inválido.
def test_delete_task_with_invalid_token(setup_create_delete_task, invalid_token):
    task_id = setup_create_delete_task
    response = delete_task(task_id, invalid_token)
    assert_delete_task_unauthorized(response)
