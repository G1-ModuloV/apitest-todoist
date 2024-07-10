import requests
from config import BASE_URI
from src.todoist_api.api_request import TodoistRequest
from src.todoist_api.endpoint import Endpoint


def get_all_comments_from_task(token, task_id):
    url = f'{BASE_URI}{Endpoint.COMMENTS.value}?task_id={task_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.get(url, headers)


def get_a_comment(token, comment_id):
    url = f'{BASE_URI}/rest/v2/comments/{comment_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)

def get_all_comments_from_project(token, project_id):
    url = f'{BASE_URI}{Endpoint.COMMENTS.value}?project_id={project_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.get(url, headers)

def create_a_comment(token, comment_body):
    url = f'{BASE_URI}/rest/v2/comments'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    return requests.post(url, headers=headers, data=comment_body)

def delete_comment(token, comment_id):
    url = f"{BASE_URI}/rest/v2/comments/{comment_id}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    return requests.delete(url, headers=headers)

def update_a_comment(token, comment_id, comment_data):
    url = f"{BASE_URI}{Endpoint.COMMENTS.value}/{comment_id}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.update(url, headers, comment_data)