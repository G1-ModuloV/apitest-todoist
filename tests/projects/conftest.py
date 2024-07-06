import pytest
import requests
import json
from src.login import get_token
from src.utils.project import update_a_project
from src.resources.payloads.update_a_project_data import project_id_update, data_origin

@pytest.fixture(scope="module")
def setup_and_teardown_update():
    token = get_token()

    # Setup
    response= update_a_project(project_id_update, json.dumps(data_origin), token)
    assert response.status_code == 200

    yield project_id_update, token, data_origin

    # Teardown
    response= update_a_project(project_id_update, json.dumps(data_origin), token)
    assert response.status_code == 200