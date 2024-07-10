import requests
from config import BASE_URI
from src.todoist_api import endpoint
from src.todoist_api.api_request import TodoistRequest
from src.todoist_api.endpoint import Endpoint


def get_all_comments_from_task(token, task_id):
    url = f'{BASE_URI}/rest/v2/comments?task_id={task_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.get(url, headers)


def get_a_comment(token, comment_id):
    url = f'{BASE_URI}{Endpoint.COMMENTS.value}/{comment_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.get(url, headers)

def get_all_comments_from_project(token, project_id):
    url = f'{BASE_URI}/rest/v2/comments?project_id={project_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.get(url, headers)

def create_a_comment(token, comment_body):
    url = f'{BASE_URI}{Endpoint.COMMENTS.value}/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    return TodoistRequest.post(url, headers, comment_body)

def delete_comment(token, comment_id):
    url = f"{BASE_URI}{Endpoint.COMMENTS.value}/{comment_id}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    return TodoistRequest.delete(url, headers)

def update_a_comment(token, comment_id, comment_data):
    url = f"{BASE_URI}/rest/v2/comments/{comment_id}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.post(url, headers, comment_data)