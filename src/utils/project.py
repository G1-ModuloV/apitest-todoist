import requests
from config import BASE_URI

def get_all_projects(token):
    url = f'{BASE_URI}/rest/v2/projects/2335308589'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)