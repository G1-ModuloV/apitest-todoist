import pytest
import json
from src.login import get_token
from src.utils.project import update_a_project
from src.resources.payloads.update_a_project_data import data_new, data_vacia, new_name, new_color, new_favorite,new_style
from src.assertions.projects.update_a_project_assertions import (assert_status_code, assert_cambio_de_parametros,
                                                                 assert_name, assert_color, assert_favorite,
                                                                 assert_style)


@pytest.mark.smoke
# TD-8 Validar actualización exitosa con todos los parámetros válidos (name, color, is_favorite, view_style)
def test_update_project_all_valid_parameters(setup_update_a_project):
    project_id_update, token, data_origin = setup_update_a_project
    response = update_a_project(project_id_update, json.dumps(data_new), get_token())
    assert_status_code(response, 200)
    assert_cambio_de_parametros(response)


@pytest.mark.smoke
# TD-8 Validar actualización del proyecto con solo el parámetro name válido
def test_update_project_name_only(setup_update_a_project):
    project_id_update, token, _ = setup_update_a_project
    response = update_a_project(project_id_update, json.dumps(new_name), get_token())
    assert_status_code(response, 200)
    assert_name(response)


@pytest.mark.smoke
# TD-8 Validar actualización del proyecto con solo el parámetro color válido
def test_update_project_color_only(setup_update_a_project):
    project_id_update, token, _ = setup_update_a_project
    response = update_a_project(project_id_update, json.dumps(new_color), get_token())
    assert_status_code(response, 200)
    assert_color(response)


@pytest.mark.smoke
# TD-8 Validar actualización del proyecto con solo el parámetro is_favorite válido
# NO PERMITE QUE SOLO SE CAMBIE "IS_FAVORITE", SE AGREGO UN PARAMETRO MAS "COLOR"'''
def test_update_project_is_favorite_only(setup_update_a_project):
    project_id_update, token, _ = setup_update_a_project
    response = update_a_project(project_id_update, json.dumps(new_favorite), get_token())
    assert_status_code(response, 200)
    print(response.status_code)
    assert_favorite(response)


@pytest.mark.smoke
# TD-8 Validar actualización del proyecto con solo el parámetro view_style válido
def test_update_project_view_style_only(setup_update_a_project):
    project_id_update, token, _ = setup_update_a_project
    response = update_a_project(project_id_update, json.dumps(new_style), get_token())
    assert_status_code(response, 200)
    assert_style(response)


@pytest.mark.smoke
# TD-8 Verificar actualización sin ningún dato
def test_update_project_no_data(setup_update_a_project):
    project_id_update, token, _ = setup_update_a_project
    response = update_a_project(project_id_update, json.dumps(data_vacia), get_token())
    assert_status_code(response, 400)
