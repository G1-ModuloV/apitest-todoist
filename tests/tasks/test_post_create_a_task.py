import pytest
from src.utils.task import create_task
from src.assertions.tasks.post_create_task_assertions import (
    assert_create_task_successful,
    assert_create_a_task_json,
)

@pytest.mark.smoke
@pytest.mark.regression
# TD-15 Verificar que una tarea pueda ser creada con todos los parámetros obligatorios.
def test_create_task_with_mandatory_fields(valid_task_data_mandatory_field, valid_token):
    response = create_task(valid_task_data_mandatory_field, valid_token)
    assert_create_task_successful(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-15 Verificar que se pueda crear una tarea utilizando varias combinaciones de parámetros opcionales (description, priority, due_string, etc.).
def test_create_task_with_optional_fields(valid_task_data_optional_fields, valid_token):
    response = create_task(valid_task_data_optional_fields, valid_token)
    assert_create_task_successful(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-15 Verificar que después de crear una tarea se reciba un body response en formato JSON.
def test_create_task_response_format(valid_task_data_mandatory_field, valid_token):
    response = create_task(valid_task_data_mandatory_field, valid_token)
    assert_create_task_successful(response)
    assert_create_a_task_json(response)


