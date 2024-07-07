import pytest
from src.utils.task import create_task, delete_task
from src.assertions.tasks.post_create_task_assertions import (
    assert_create_task_successful,
    assert_create_a_task_json,
    assert_create_task_bad_request,
    assert_create_task_unauthorized
)


@pytest.mark.smoke
@pytest.mark.regression
# TD-15 Verificar que una tarea pueda ser creada con todos los parámetros obligatorios.
def test_create_task_with_mandatory_fields(valid_task_data_mandatory_field, valid_token):
    response = create_task(valid_task_data_mandatory_field, valid_token)
    assert_create_task_successful(response)
    task_id = response.json()['id']
    delete_task(task_id, valid_token)


@pytest.mark.smoke
@pytest.mark.regression
# TD-15 Verificar que se pueda crear una tarea utilizando varias combinaciones de parámetros opcionales (description, priority, due_string, etc.).
def test_create_task_with_optional_fields(valid_task_data_optional_fields, valid_token):
    response = create_task(valid_task_data_optional_fields, valid_token)
    assert_create_task_successful(response)
    task_id = response.json()['id']
    delete_task(task_id, valid_token)


@pytest.mark.smoke
@pytest.mark.regression
# TD-15 Verificar que después de crear una tarea se reciba un body response en formato JSON.
def test_create_task_response_format(valid_task_data_mandatory_field, valid_token):
    response = create_task(valid_task_data_mandatory_field, valid_token)
    assert_create_task_successful(response)
    assert_create_a_task_json(response)
    task_id = response.json()['id']
    delete_task(task_id, valid_token)


@pytest.mark.regression
# TD-15 Verificar que no se pueda crear una tarea sin el parámetro obligatorio "content".
def test_create_task_without_mandatory_param(incomplete_task_data, valid_token):
    response = create_task(incomplete_task_data, valid_token)
    assert_create_task_bad_request(response)


@pytest.mark.regression
# TD-15 Verificar que no se pueda crear una tarea con un token de autorización inválido
def test_create_task_with_invalid_token(valid_task_data_optional_fields, invalid_token):
    response = create_task(valid_task_data_optional_fields, invalid_token)
    assert_create_task_unauthorized(response)


@pytest.mark.regression
# TD-15 Verificar que no se pueda crear una tarea sin token de autorización
def test_create_task_without_token(valid_task_data_mandatory_field, no_token):
    response = create_task(valid_task_data_mandatory_field, no_token)
    assert_create_task_unauthorized(response)
