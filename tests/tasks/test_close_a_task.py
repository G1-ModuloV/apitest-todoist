import pytest
from src.utils.task import close_a_task
from src.login import get_token
from src.assertions.schema_assertion import assert_schema
from src.assertions.tasks.close_a_task_assertions import (
    assert_post_close_task_success,
    assert_post_close_task_bad_request,
    assert_post_task_not_found,
    assert_post_close_task_unauthorized)


@pytest.mark.smoke
@pytest.mark.regression
# TD-17 Verificar que la respuesta sea exitosa al cerrar una tarea con un token valido y un id de tarea valido - SMOKE
def test_post_close_a_task_token_valid_id_valid(valid_token, setup_close_a_task):
    task_id = setup_close_a_task
    response = close_a_task(valid_token, task_id)
    assert_post_close_task_success(response)



@pytest.mark.smoke
@pytest.mark.regression
# TD-17 Verificar que la respuesta sea erronea al cerrar una tarea con un token Invalido y un id de tarea valido - SMOKE
def test_post_close_a_task_token_invalid_id_valid(invalid_token, setup_close_a_task):
    task_id = setup_close_a_task
    response = close_a_task(invalid_token, task_id)
    assert_post_close_task_unauthorized(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-17 Verificar que la respuesta sea erronea al cerrar una tarea con un token valido y un id de tarea Invalido - SMOKE
def test_post_close_a_task_token_valid_id_invalid(valid_token, nonexistent_task_id):
    response = close_a_task(valid_token, nonexistent_task_id)
    assert_post_task_not_found(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-17 Verificar que la respuesta sea erronea al cerrar una tarea con un token invalido y un id de tarea Invalido - SMOKE
def test_post_close_a_task_token_invalid_id_invalid(invalid_token, nonexistent_task_id):
    response = close_a_task(invalid_token, nonexistent_task_id)
    assert_post_close_task_unauthorized(response)

