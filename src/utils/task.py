import requests
from config import BASE_URI


def get_a_task(task_id, token):
    url = f"{BASE_URI}/rest/v2/tasks/{task_id}"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)



def create_task(task_data, token):
    url = f"{BASE_URI}/rest/v2/tasks"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    return requests.post(url, headers=headers, json=task_data)


def delete_task(task_id, token):
    url = f"{BASE_URI}/rest/v2/tasks/{task_id}"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.delete(url, headers=headers)

def get_tasks(token):
    url = f"{BASE_URI}/rest/v2/tasks"
    headers = {
        'Authorization': f'Bearer {token}',
  }
    return requests.get(url, headers=headers)

def get_tasks_from_project(token, valid_project_id):
    url = f'{BASE_URI}/rest/v2/tasks?project_id={valid_project_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)

def get_tasks_from_seccion(token, valid_project_id, valid_section_id):
    url = f'{BASE_URI}/rest/v2/tasks?project_id={valid_project_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)

def update_a_task(task_id, payload, token):
  url = f"https://api.todoist.com/rest/v2/tasks/{task_id}"
  headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
  }
  return requests.request("POST", url, headers=headers, data=payload)


def reopen_a_task(task_id, token):
  url = f"{BASE_URI}/rest/v2/tasks/{task_id}/reopen"
  headers = {
    'Authorization': f'Bearer {token}',
  }
  return requests.post(url, headers=headers)


def close_a_task(token, task_id):
    url = f"{BASE_URI}/rest/v2/tasks/{task_id}/close"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.request("POST", url, headers=headers)


