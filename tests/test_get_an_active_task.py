import pytest
import requests
from src.utils.task import get_a_task
from src.login import get_token

from jsonschema import validate

url = "https://api.todoist.com/rest/v2/tasks/8157539480"
headers = {
    'Authorization' : 'Bearer 70b0647e981e2daa4ee6c5ab66d44a34adc00536'
}

json_schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "creator_id": {"type": ["null", "string"]},
            "created_at": {"type": "string"},
            "assignee_id": {"type": ["null", "string"]},
            "assigner_id": {"type": ["null", "string"]},
            "comment_count": {"type": "integer"},
            "is_completed": {"type": "boolean"},
            "content": {"type": "string"},
            "description": {"type": "string"},
            "due": {
                "type": ["null", "object"],
                "properties": {
                    "date": {"type": "string"},
                    "is_recurring": {"type": "boolean"},
                    "datetime": {"type": ["null", "string"]},
                    "string": {"type": "string"},
                    "timezone": {"type": ["null", "string"]}
                },
                "required": ["date", "is_recurring", "string"]
            },
            "duration": {"type": ["null", "object"]},
            "id": {"type": "string"},
            "labels": {
                "type": "array",
                "items": {"type": "string"}
            },
            "order": {"type": "integer"},
            "priority": {"type": "integer"},
            "project_id": {"type": "string"},
            "section_id": {"type": ["null", "string"]},
            "parent_id": {"type": ["null", "string"]},
            "url": {"type": "string"}
        },
        "required": [
            "creator_id", "created_at", "comment_count", "is_completed",
            "content", "description", "id", "labels", "order",
            "priority", "project_id", "url"
        ]
    }

def test_get_an_active_task():

    response = get_a_task("8160389085",get_token())
    assert response.status_code == 200


def test_get_an_active_task_schema():
    response = get_a_task("8160389085",get_token())
    assert response.status_code == 200

    validate(instance=response.json(), schema=json_schema)
