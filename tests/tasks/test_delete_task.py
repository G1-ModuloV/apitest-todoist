import pytest
from src.utils.task import delete_task
from src.assertions.tasks.delete_a_task_assertions import (
    assert_delete_task_successful,
    assert_delete_task_unauthorized
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
