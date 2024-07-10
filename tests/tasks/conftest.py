import pytest
import requests
import json
from config import BASE_URI
from src.resources.payloads.reopen_a_task_data import data_reopen_task_create
from src.resources.payloads.close_a_task_data import data_close_task_creation
from src.utils.task import create_task, delete_task, close_a_task, update_a_task


@pytest.fixture(scope="session")
def valid_task_data_mandatory_field():
    return {
        "content": "Test nueva tarea"
    }


@pytest.fixture(scope="session")
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
def setup_create_delete_task(valid_task_data_mandatory_field, valid_token):
    response = create_task(valid_task_data_mandatory_field, valid_token)
    task_id = response.json()['id']

    def teardown():
        delete_task(task_id, valid_token)

    yield task_id
    teardown()


@pytest.fixture(scope="session")
def setup_close_a_task(valid_task_data_mandatory_field, valid_token):
    #Create a task
    response = create_task(data_close_task_creation, valid_token)
    task_id = response.json()['id']
    #close a task
    close_a_task(valid_token, task_id)
    # delete a task
    def teardown():
        delete_task(task_id, valid_token)

    yield task_id
    teardown()


@pytest.fixture
def nonexistent_task_id():
    return "2587410360"




@pytest.fixture(scope="session")
def setup_reopen_task(valid_task_data_mandatory_field, valid_token):
    # Setup
    # Create task
    response = create_task(data_reopen_task_create, valid_token)
    task_id = response.json()['id']

    # Close task
    close_a_task(valid_token, task_id)

    yield task_id

    # teardown
    #delete task
    delete_task(task_id, valid_token)


@pytest.fixture(scope="session")
def setup_create_delete_task_optional_fields(valid_task_data_optional_fields, valid_token):
    response = create_task(valid_task_data_optional_fields, valid_token)
    task_id = response.json()['id']

    def teardown():
        delete_task(task_id, valid_token)

    yield task_id
    teardown()
