import pytest
import json
from src.utils.label import delete_a_label, create_a_personal_label
from src.utils.task import create_task, delete_task, update_a_task
from src.resources.payloads.rename_share_labels_data import label_payload, updated_task_payload, task_payload


def get_label_id(token):
    response = create_a_personal_label(json.dumps(label_payload), token)
    response_data = response.json()
    return response_data["id"]


@pytest.fixture(scope="session")
def setup_create_a_label(valid_token):
    label_id = get_label_id(valid_token)

    def teardown():
        delete_a_label(label_id, valid_token)

    yield label_id
    teardown()
    return label_id


@pytest.fixture
def nonexistent_label_id():
    return "2173775788"


@pytest.fixture(scope="session")
def setup_create_a_task(valid_token):
    response = create_task(task_payload, valid_token)
    response_data = response.json()
    task_id = response_data["id"]

    def teardown():
        delete_task(task_id, valid_token)

    yield task_id
    teardown()
    return task_id


@pytest.fixture(scope="function")
def setup_create_a_shared_label(valid_token, setup_create_a_task):
    label_id = get_label_id(valid_token)
    update_a_task(setup_create_a_task, json.dumps(updated_task_payload), valid_token)

    def teardown():
        delete_a_label(label_id, valid_token)

    yield label_id
    teardown()
    return label_id


@pytest.fixture(scope="function")
def setup_create_an_extra_label(valid_token):
    label_id = get_label_id(valid_token)

    def teardown():
        delete_a_label(label_id, valid_token)

    yield label_id
    teardown()
    return label_id
