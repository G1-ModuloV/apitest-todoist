import pytest
from src.login import get_token
import requests
import jsonschema
from src.utils.project import get_all_projects

# 1)  @Automation    @Functional    @Smoke       @Validar la obtención de todos los proyectos con un token de autenticación válido
def test_get_all_projects_valid_token():
    response = get_all_projects(get_token())
    # Verificar que la respuesta tiene un estado 200 OK
    assert response.status_code == 200, "Expected status code 200 OK"
    # Verificar que la respuesta contiene un array JSON con los proyectos del usuario
    assert isinstance(response.json(), list), "Expected response to be a JSON array"


# 7)  @Automation    @Functional    @Smoke       @Validar que el Content-Type de la respuesta es application/json
def test_content_type_is_json():
    response = get_all_projects(get_token())
    # Verificar que el Content-Type de la respuesta es application/json
    assert response.headers["Content-Type"] == "application/json", "Expected Content-Type application/json"

# 8)  @Automation    @Functional    @Smoke       @Validar que la respuesta tiene el estado 200 OK para una solicitud exitosa
def test_response_status_is_200():
    response = get_all_projects(get_token())

    # Verificar que la respuesta tiene un estado 200 OK
    assert response.status_code == 200, "Expected status code 200 OK"

