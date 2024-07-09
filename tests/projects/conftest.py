import pytest
import json
from src.login import get_token
from src.utils.project import update_a_project, post_a_project, delete_a_project
from src.resources.payloads.create_a_project_data import get_project_data
from src.resources.payloads.update_a_project_data import project_id_update, data_origin


@pytest.fixture(scope="session")
def setup_update_a_project():
    token = get_token()

    response = update_a_project(project_id_update, json.dumps(data_origin), token)

    def teardown():
        response = update_a_project(project_id_update, json.dumps(data_origin), token)

    yield project_id_update, token, data_origin
    teardown()


@pytest.fixture(scope="function")
def setup_create_project(valid_token, request):
    def create_project_with_data(data_key):
        data = get_project_data(data_key)
        response = post_a_project(valid_token, data)
        if response.status_code == 403:
            pytest.skip("Maximum number of projects")
        project_id = response.json()["id"]

        def teardown():
            delete_a_project(valid_token, project_id)

        request.addfinalizer(teardown)

        return response, project_id

    return create_project_with_data


@pytest.fixture(scope="function")
def setup_delete_project(valid_token):
    data = {"name": "Test delete a project"}
    response = post_a_project(valid_token, data)
    project_id = response.json()["id"]

    def teardown():
        delete_a_project(valid_token, project_id)

    yield project_id
    teardown()
