import pytest
from src.utils.task import reopen_a_task
from src.assertions.tasks.reopen_a_task_assertions import assert_reopen_task_value_success, assert_reopen_task_unauthorized

@pytest.mark.smoke
@pytest.mark.regression
# TD-19 Verificar que se reabra una tarea con id valido
def test_reopen_task(setup_reopen_task, valid_token):
    task_id = setup_reopen_task
    response = reopen_a_task(task_id, valid_token)
    assert_reopen_task_value_success(response, task_id, valid_token)

@pytest.mark.smoke
@pytest.mark.regression
# TD-19 Verificar que no se pueda reabrir una tarea dando un token de autorizacion invalido
def test_reopen_task_with_invalid_token(setup_reopen_task, invalid_token):
    task_id = setup_reopen_task
    response = reopen_a_task(task_id, invalid_token)
    assert_reopen_task_unauthorized(response)

@pytest.mark.smoke
@pytest.mark.regression
# TD-19 Verificar que no se pueda reabrir una tarea sin dar un token de autorizacion
def test_reopen_task_without_token(setup_reopen_task, no_token):
    task_id = setup_reopen_task
    response = reopen_a_task(task_id, no_token)
    assert_reopen_task_unauthorized(response)