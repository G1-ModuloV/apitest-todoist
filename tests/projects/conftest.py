import pytest
import json
from src.login import get_token
from src.utils.project import update_a_project
from src.resources.payloads.update_a_project_data import project_id_update, data_origin


@pytest.fixture(scope="session")
def setup_update_a_project():
    token = get_token()

    response= update_a_project(project_id_update, json.dumps(data_origin), token)

    def teardown():
        response = update_a_project(project_id_update, json.dumps(data_origin), token)

    yield project_id_update, token, data_origin
    teardown()
