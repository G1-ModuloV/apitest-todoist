import pytest
import requests

from config import BASE_URI, EMAIL, PASSWORD


def get_response_login():
    url = f'{BASE_URI}/api/v9.1/user/login'
    payload = {
        "email": EMAIL,
        "password": PASSWORD
    }
    headers = {
        'doist-platform': 'web'
    }

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code ==200
    return response.json()
def get_token():
    response_data = get_response_login()
    token = response_data.get("token", None)
    return token
