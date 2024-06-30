import requests
from config import BASE_URI


def get_a_project(token, project_id):
    url = f'{BASE_URI}/rest/v2/projects/{project_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)

def get_all_projects(token):
    url = f'{BASE_URI}/rest/v2/projects'
    headers = {
         'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)
