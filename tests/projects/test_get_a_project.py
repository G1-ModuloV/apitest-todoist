import pytest
import jsonschema
from src.login import get_token
from src.utils.project import get_all_projects
from src.assertions.projects.get_a_project_assertions import assert_get_a_project_code_200, assert_get_a_project_json

#Verificar respuesta exitosa con un ID de proyecto válido
def test_get_a_project_tc01():
    response = get_all_projects(get_token())
    assert_get_a_project_code_200(response)
#Verificar que el objeto JSON en la respuesta contenga los campos esperados
def test_get_a_project_tc02():
    response = get_all_projects(get_token())
    assert_get_a_project_json(response)