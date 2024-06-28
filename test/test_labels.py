import pytest
import jsonschema
from src.login import token
from src.utils.label import get_all_labels


def test_get_all_labels():
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "order": {
                    "type": "integer"
                },
                "color": {
                    "type": "string"
                },
                "is_favorite": {
                    "type": "boolean"
                }
            },
            "required": ["id", "name", "order", "color", "is_favorite"]
        }
    }
    response = get_all_labels(token())
    response_data = response.json()
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
