import pytest
import requests
import json
from config import BASE_URI


@pytest.fixture(scope="session")
def setup_teardown_update_comment(valid_token):
    # set up
    # el codigo siguiente que crea el comentario sera posteriormente reemplazado por el metodo respectivo en utils que sera creado
    url = f"{BASE_URI}/rest/v2/comments"
    headers = {
        'Authorization': f'Bearer {valid_token}',
        'Content-Type': 'application/json',
    }
    payload = {
        "content": "task comment automated 1",
        "task_id": 8153939895
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response_data = response.json()
    comment_id = response_data["id"]

    yield comment_id

    # teardown
    #
    # el codigo siguiente que elimina el comentario sera posteriormente reemplazado por el metodo respectivo en utils que sera creado
    requests.delete(f"{url}/{comment_id}", headers=headers)