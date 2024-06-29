import pytest
import jsonschema
from src.login import get_token
from src.utils.comment import get_all_comments


def test_get_all_comments():
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "task_id": {
                        "type": "string"
                    },
                    "project_id": {
                        "type": "null"
                    },
                    "content": {
                        "type": "string"
                    },
                    "posted_at": {
                        "type": "string"
                    },
                    "attachment": {
                        "type": "null"
                    }
                },
                "required": [
                    "id",
                    "task_id",
                    "project_id",
                    "content",
                    "posted_at",
                    "attachment"
                ]
            }
        ]
    }
    response = get_all_comments(get_token())
    response_data = response.json()
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
