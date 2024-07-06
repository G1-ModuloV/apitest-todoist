import pytest
import json
from src.login import get_token
from src.utils.project import update_a_project
from src.resources.payloads.update_a_project_data import project_id_update, data_origin, data_new, data_vacia
from src.assertions.projects.update_a_project_assertions import (assert_status_code,assert_cambio_de_parametros,
                                                                 assert_name, assert_color, assert_favorite, assert_style)


@pytest.mark.smoke
#TD-8-1 Validar actualización exitosa con todos los parámetros válidos (name, color, is_favorite, view_style)
def test_update_project_all_valid_parameters(setup_and_teardown_update):
    project_id_update, token, data_origin = setup_and_teardown_update
    response = update_a_project(project_id_update, json.dumps(data_new), get_token())
    print("Ahora es:", response.text)
    assert_status_code(response, 200)
    assert_cambio_de_parametros(response)

@pytest.mark.smoke
#TD-8-2 Validar actualización del proyecto con solo el parámetro name válido
def test_update_project_name_only(setup_and_teardown_update):
    project_id_update, token, _ = setup_and_teardown_update
    data = {"name": "New Project Name"}
    response = update_a_project(project_id_update,json.dumps(data), get_token())
    assert_status_code(response, 200)
    assert_name(response)
    #print("Ahora es:", response.json()["name"])

@pytest.mark.smoke
#TD-8-3 Validar actualización del proyecto con solo el parámetro color válido
def test_update_project_color_only(setup_and_teardown_update):
    project_id_update, token, _ = setup_and_teardown_update
    data = {"color": "yellow"}
    response = update_a_project(project_id_update, json.dumps(data), get_token())
    assert_status_code(response, 200)
    assert_color(response)
    # print("Ahora es:", response.json()["color"])

@pytest.mark.smoke
#TD-8-4 Validar actualización del proyecto con solo el parámetro is_favorite válido
#NO PERMITE QUE SOLO SE CAMBIE "IS_FAVORITE", SE AGREGO UN PARAMETRO MAS "COLOR"'''
def test_update_project_is_favorite_only(setup_and_teardown_update):
    project_id_update, token, _ = setup_and_teardown_update
    data = {"color": "red",
            "is_favorite": False}
    response = update_a_project(project_id_update, json.dumps(data), get_token())
    assert_status_code(response, 200)
    assert_favorite(response)
    #print("Ahora es:", response.json()["is_favorite"])

@pytest.mark.smoke
#TD-8-5 Validar actualización del proyecto con solo el parámetro view_style válido
def test_update_project_view_style_only(setup_and_teardown_update):
    project_id_update, token, _ = setup_and_teardown_update
    data = {"view_style": "board"}
    response = update_a_project(project_id_update, json.dumps(data), get_token())
    assert_status_code(response, 200)
    assert_style(response)
    # print("Ahora es:", response.json()["view_style"])

@pytest.mark.funcional
@pytest.mark.smoke
#TD-8-6 Verificar actualización sin ningún dato
def test_update_project_no_data(setup_and_teardown_update):
    project_id_update, token, _ = setup_and_teardown_update
    response = update_a_project(project_id_update, json.dumps(data_vacia), get_token())
    assert_status_code(response, 400)
    #print("Ahora es:", response.text)