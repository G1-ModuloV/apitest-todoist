import pytest
from src.login import get_token
from src.utils.project import get_a_project
from src.assertions.projects.get_a_project_assertions import assert_get_a_project_code_200,assert_get_a_project_json


#Verificar respuesta exitosa con un ID de proyecto válido
def  test_get_a_project_successful_response(valid_token, valid_project_id):
    response = get_a_project(valid_token, valid_project_id)
    assert_get_a_project_code_200(response)


#Verificar que el objeto JSON en la respuesta contenga los campos esperados
def test_get_a_project_valid_json(valid_token, valid_project_id):
    response = get_a_project(valid_token, valid_project_id)
    assert_get_a_project_json(response, valid_project_id)



