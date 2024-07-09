import pytest
from src.utils.project import post_a_project, post_a_project_with_data_invalid, post_a_project_with_using_get, \
    post_a_project_with_wrong_content_type
from src.assertions.projects.create_a_new_project_assertions import assert_status_code, assert_content_type, assert_json_contains
from src.resources.payloads.create_a_project_data import get_project_data
from src.utils.project import post_a_project_with_id


@pytest.mark.smoke
@pytest.mark.regression
# TD-7 Verificar respuesta exitosa al crear un nuevo proyecto con solo el nombre
def test_create_project_with_name(setup_create_project):
    response, _ = setup_create_project("valid_name")
    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_json_contains(response, "id")


@pytest.mark.smoke
@pytest.mark.regression
# TD-7 Verificar respuesta exitosa al crear un nuevo proyecto con nombre y color
def test_create_project_with_name_and_color(setup_create_project):
    response, _ = setup_create_project("with_color")
    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_json_contains(response, "id")


@pytest.mark.smoke
@pytest.mark.regression
# TD-7 Verificar respuesta exitosa al crear un nuevo proyecto como favorito
def test_create_project_as_favorite(setup_create_project):
    response, _ = setup_create_project("with_is_favorite")
    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_json_contains(response, "id")


@pytest.mark.smoke
@pytest.mark.regression
# TD-7 Verificar respuesta exitosa al crear un nuevo proyecto con estilo de vista
def test_create_project_with_view_style(setup_create_project):
    response, _ = setup_create_project("with_view_style")
    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_json_contains(response, "id")


@pytest.mark.smoke
@pytest.mark.regression
# TD-7 Verificar respuesta exitosa al crear un nuevo proyecto con un ID de proyecto existente
def test_create_project_with_parent_id(setup_create_project,valid_token):
    project_id = setup_create_project("valid_name")
    response = post_a_project_with_id(valid_token,project_id)
    assert_status_code(response, 400)


@pytest.mark.regression
# TD-7 Verificar respuesta con token de autorización inválido
def test_create_project_with_invalid_token(invalid_token):
    data = get_project_data("valid_name")
    response = post_a_project(invalid_token, data)
    assert_status_code(response, 401)


@pytest.mark.regression
# TD-7 Verificar respuesta sin token de autorización
def test_create_project_without_token(no_token):
    data = get_project_data("valid_name")
    response = post_a_project(no_token, data)
    assert_status_code(response, 401)


@pytest.mark.regression
# TD-7 Verificar respuesta con formato incorrecto del cuerpo de la solicitud
def test_create_project_with_invalid_body_format(valid_token,setup_create_project):
    project_id = setup_create_project("valid_name")
    response= post_a_project_with_data_invalid(valid_token, project_id)
    assert_status_code(response, 400)


@pytest.mark.regression
# TD-7 Verificar respuesta cuando el contenido del cuerpo de la solicitud está vacío
def test_create_project_with_empty_body(valid_token):
    data = {}
    response = post_a_project(valid_token, data)
    assert_status_code(response, 400)


@pytest.mark.regression
# TD-7 Verificar respuesta con método HTTP incorrecto (GET en lugar de POST)
def test_create_project_with_wrong_http_method(valid_token, setup_create_project):
    project_id = setup_create_project("valid_name")
    response = post_a_project_with_using_get(valid_token, project_id)
    assert_status_code(response, 400)


@pytest.mark.regression
# TD-7 Verificar respuesta con encabezado Content-Type incorrecto
def test_create_project_with_wrong_content_type(valid_token,setup_create_project):
    project_id = setup_create_project("valid_name")
    response= post_a_project_with_wrong_content_type(valid_token,project_id)
    assert_status_code(response, 400)


@pytest.mark.regression
# TD-7 Verificar la respuesta con un nombre de proyecto que ya existe
def test_create_project_with_existing_name(valid_token, setup_create_project):
    response, _ = setup_create_project("valid_name")
    assert_status_code(response, 200)
    response = post_a_project(valid_token, get_project_data("valid_name"))
    assert_status_code(response, 200)