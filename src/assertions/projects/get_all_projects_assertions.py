from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema
import pytest

def assert_status_code(response,aux):
    assert response.status_code == aux

def assert_list(response):
    try:
        json_data = response.json()
        assert isinstance(json_data, list)
    except ValueError:
        pytest.fail("Error: La respuesta no es JSON válida")

def assert_cotent_type_es_json(response):
    schema = read_a_json("projects_schema.json")
    assert_schema(response, schema)
    assert response.headers["Content-Type"] == "application/json", "El Content-Type es application/json"

def assert_mensaje_error(response):
    assert response.json().get('error') is not None

def assert_ASCII(response):
    json_data = response.json()
    if json_data:
        for project in json_data:
            assert isinstance(json_data['name'], str)
            # Verificar que el nombre contiene caracteres ASCII válidos
            assert all(ord(char) < 128 for char in json_data['name'])
    else:
        pytest.skip("No hay proyectos disponibles para verificar")

def assert_tamanio_nombre(response):
    json_data = response.json()
    for project in json_data:
        assert 1 <= len(project['name']) < 110

def assert_any_project(response):
    json_data = response.json()
    # Verificar que la respuesta es una lista
    assert_list(response)
    if not json_data:
        # Si la lista está vacía, la prueba es exitosa
        assert json_data == [], "Se esperaba una lista vacía cuando no hay proyectos disponibles"
    else:
        # Si la lista no está vacía, omitir la prueba
        pytest.skip("La lista de proyectos no está vacía, omitiendo prueba")

def assert_projects(response):
    for project in response.json():
        assert 'parent_id' in project, "Se esperaba que el proyecto tuviera un campo parent_id"
        if project['parent_id']:
            assert isinstance(project['parent_id'], int), "Se esperaba que parent_id fuera un entero o null"

def assert_filtro(response,filters):
    json_data = response.json()
    matched_projects = [project for project in json_data if filters["color"] == project['color']]
    assert matched_projects, f"No se encontró ningún proyecto con el nombre '{filters['name']}'"
    '''for project in matched_projects:
        if filters.get("is_favorite") is not None:
            assert project['is_favorite'] == filters["is_favorite"], f"Se esperaba que el proyecto {'fuera favorito' if filters['is_favorite'] else 'no fuera favorito'}, pero no lo es: {project['name']}"
    '''