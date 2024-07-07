import pytest
from src.utils.task import create_task, delete_task


@pytest.fixture(scope="session")
def valid_task_data_mandatory_field():
    return {
        "content": "Test nueva tarea"
    }


@pytest.fixture
def valid_task_data_optional_fields():
    return {
        "content": "Tarea con campos opcionales",
        "description": "Esta tarea es con campos opcionales",
        "due_date": "2024-07-10"
    }


@pytest.fixture
def incomplete_task_data():
    return {
        "description": "Nueva descripción",
        "due_date": "2024-07-10"
    }


@pytest.fixture(scope="session")
def setup_create_task(valid_task_data_mandatory_field, valid_token):
    response = create_task(valid_task_data_mandatory_field, valid_token)
    task_id = response.json()['id']

    def teardown():
        delete_task(task_id, valid_token)

    yield task_id
    teardown()
