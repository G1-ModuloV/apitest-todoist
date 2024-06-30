import pytest
from src.login import get_token
import requests
import jsonschema
from src.utils.project import get_all_projects
from src.assertions.projects.get_all_projects_assertions import assert_code_200, assert_array, assert_cotent_type_es_json

# 1)  @Automation    @Functional    @Smoke       @Validar la obtención de todos los proyectos con un token de autenticación válido
def test_get_all_projects_valid_token():
    response = get_all_projects(get_token())
    assert_array(response)
    assert_code_200(response)


# 7)  @Automation    @Functional    @Smoke       @Validar que el Content-Type de la respuesta es application/json
def test_content_type_is_json():
    response = get_all_projects(get_token())
    assert_cotent_type_es_json(response)

# 8)  @Automation    @Functional    @Smoke       @Validar que la respuesta tiene el estado 200 OK para una solicitud exitosa
def test_response_status_is_200():
    response = get_all_projects(get_token())
    assert_code_200(response)

