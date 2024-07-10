import pytest
import json
from src.utils.project import update_a_project
from src.resources.payloads.update_a_project_data import data_new, data_vacia, new_name, new_color, new_favorite, new_style
from src.assertions.projects.update_a_project_assertions import (assert_status_code, assert_cambio_de_parametros,
                                                                 assert_name, assert_color, assert_favorite,
                                                                 assert_style)


@pytest.mark.regression
@pytest.mark.smoke
# TD-8 Validar actualización exitosa con todos los parámetros válidos (name, color, is_favorite, view_style)
def test_update_project_all_valid_parameters(setup_create_project, valid_token):
    _, project_id = setup_create_project("valid_name")
    response = update_a_project(project_id, json.dumps(data_new), valid_token)
    assert_status_code(response, 200)
    assert_cambio_de_parametros(response)


@pytest.mark.regression
@pytest.mark.smoke
# TD-8 Validar actualización del proyecto con solo el parámetro name válido
def test_update_project_name_only(setup_create_project, valid_token):
    _, project_id = setup_create_project("valid_name")
    response = update_a_project(project_id, json.dumps(new_name), valid_token)
    assert_status_code(response, 200)
    assert_name(response)


@pytest.mark.regression
@pytest.mark.smoke
# TD-8 Validar actualización del proyecto con solo el parámetro color válido
def test_update_project_color_only(setup_create_project, valid_token):
    _, project_id = setup_create_project("valid_name")
    response = update_a_project(project_id, json.dumps(new_color), valid_token)
    assert_status_code(response, 200)
    assert_color(response)


@pytest.mark.regression
@pytest.mark.smoke
# TD-8 Validar actualización del proyecto con solo el parámetro is_favorite válido
# NO PERMITE QUE SOLO SE CAMBIE "IS_FAVORITE", SE AGREGO UN PARAMETRO MAS "COLOR"'''
def test_update_project_is_favorite_only(setup_create_project, valid_token):
    _, project_id = setup_create_project("valid_name")
    response = update_a_project(project_id, json.dumps(new_favorite), valid_token)
    assert_status_code(response, 200)
    print(response.status_code)
    assert_favorite(response)


@pytest.mark.regression
@pytest.mark.smoke
# TD-8 Validar actualización del proyecto con solo el parámetro view_style válido
def test_update_project_view_style_only(setup_create_project, valid_token):
    _, project_id = setup_create_project("valid_name")
    response = update_a_project(project_id, json.dumps(new_style), valid_token)
    assert_status_code(response, 200)
    assert_style(response)


@pytest.mark.regression
@pytest.mark.smoke
# TD-8 Verificar actualización sin ningún dato
def test_update_project_no_data(setup_create_project, valid_token):
    _, project_id = setup_create_project("valid_name")
    response = update_a_project(project_id, json.dumps(data_vacia), valid_token)
    assert_status_code(response, 400)
