import pytest
import json
from src.utils.label import delete_a_label, create_a_personal_label, remove_a_shared_label
from src.utils.task import create_task, delete_task, update_a_task
from src.resources.payloads.rename_share_labels_data import label_payload, updated_task_payload, task_payload
from src.resources.payloads.create_label_data import (label_name, label_data, label_data2, label_payload2,
                                                      task_payload2, updated_task_payload2)


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


@pytest.fixture(scope="session")
def setup_create_personal_label(valid_token):
    response = create_a_personal_label(json.dumps(label_name), valid_token)
    response_data = response.json()
    label_id = response_data["id"]

    def teardown():
        delete_a_label(label_id, valid_token)

    yield label_id
    teardown()
    return label_id


@pytest.fixture(scope="session")
def setup_create_personal_label_all_valid(valid_token):
    response = create_a_personal_label(json.dumps(label_data), valid_token)
    response_data = response.json()
    label_id = response_data["id"]

    def teardown():
        delete_a_label(label_id, valid_token)

    yield label_id
    teardown()
    return label_id


@pytest.fixture(scope="session")
def setup_create_personal_label_is_favorite(valid_token):
    response = create_a_personal_label(json.dumps(label_data2), valid_token)
    response_data = response.json()
    label_id = response_data["id"]

    def teardown():
        delete_a_label(label_id, valid_token)

    yield label_id
    teardown()
    return label_id


@pytest.fixture(scope="session")
def setup_create_a_task_for_label(valid_token):
    response = create_task(task_payload2, valid_token)
    response_data = response.json()
    task_id = response_data["id"]

    def teardown():
        delete_task(task_id, valid_token)

    yield task_id
    teardown()
    return task_id


@pytest.fixture(scope="function")
def setup_create_a_shared_label_for_remove(valid_token, setup_create_a_task_for_label):
    response = create_a_personal_label(json.dumps(label_payload2), valid_token)
    response_data = response.json()
    label_result = response_data["name"]
    label_result = {"name": label_result}
    update_a_task(setup_create_a_task_for_label, json.dumps(updated_task_payload2), valid_token)

    def teardown():
        remove_a_shared_label(label_result, valid_token)
        delete_a_label(response_data["id"], valid_token)

    yield label_result
    teardown()
    return label_result
