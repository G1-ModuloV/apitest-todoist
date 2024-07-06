import pytest
import requests
import json
from config import BASE_URI
from src.utils.label import delete_a_label


@pytest.fixture(scope="session")
def get_valid_label_id(valid_token):
    url = f"{BASE_URI}/rest/v2/labels"
    headers = {
        'Authorization': f'Bearer {valid_token}',
        'Content-Type': 'application/json',
    }
    payload = {
        "name": "Food"
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response_data = response.json()
    label_id = response_data["id"]

    def teardown():
        delete_a_label(label_id, valid_token)

    yield label_id
    teardown()
    return label_id
