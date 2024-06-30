from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema
import pytest

def assert_code_200(response):
    assert response.status_code == 200, "Estado de codigo 200 OK"

def assert_array(response):
    try:
        json_data = response.json()
        assert isinstance(json_data, list), "Se esperaba que la respuesta fuera un array JSON"
    except ValueError:
        pytest.fail("Error: La respuesta no es JSON válida")

def assert_cotent_type_es_json(response):
    assert response.headers["Content-Type"] == "application/json", "El Content-Type es application/json"