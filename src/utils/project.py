import requests
from config import BASE_URI

def get_a_project(token):
    url = f'{BASE_URI}/rest/v2/projects/2335308589'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)