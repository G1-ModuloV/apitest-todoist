import pytest
from src.login import get_token
from src.utils.project import get_all_projects
from src.assertions.projects.get_all_projects_assertions import assert_status_code, assert_list, assert_cotent_type_es_json, assert_mensaje_error, assert_ASCII, assert_tamanio_nombre, assert_any_project, assert_projects,assert_filtro

@pytest.mark.smoke
# 1) Validar la obtención de todos los proyectos con un token de autenticación válido
def test_get_all_projects_with_valid_token():
    response = get_all_projects(get_token())
    assert_list(response)
    assert_status_code(response,200)
@pytest.mark.regression
# 2) Verificar el mensaje de error con un token de autenticación inválido
def test_get_all_projects_with_invalid_token():
    invalid_token = "123"
    response = get_all_projects(invalid_token)
    assert_status_code(response, 401)

'''
@pytest.mark.regression
# 3) Verificar la respuesta cuando no hay proyectos disponibles
def test_no_projects():
    response = get_all_projects(get_token())
    assert_status_code(response, 200)
    assert_any_project(response)
'''

@pytest.mark.regression
# 6) Verificar la respuesta de la API con un token de autenticación expirado
def test_expired_token():
    expired_token = "4b135b0ba9400ccb273f849444ec605d2e6b8500"
    response = get_all_projects(expired_token)
    assert_status_code(response,401)

@pytest.mark.smoke
# 7) Validar que el Content-Type de la respuesta es application/json
def test_content_type_is_json():
    response = get_all_projects(get_token())
    assert_cotent_type_es_json(response)

@pytest.mark.smoke
# 8) Validar que la respuesta tiene el estado 200 OK para una solicitud exitosa
def test_response_status_is_200():
    response = get_all_projects(get_token())
    assert_status_code(response,200)

@pytest.mark.regression
# 9) Verificar la longitud máxima y mínima del nombre del proyecto
def test_project_name_length():
    response = get_all_projects(get_token())
    assert_status_code(response,200)
    assert_tamanio_nombre(response)


@pytest.mark.regression
# 10) Validar la obtención de proyectos con proyectos anidados o subproyectos
def test_nested_projects():
    response = get_all_projects(get_token())
    assert_status_code(response,200)
    assert_projects(response)


@pytest.mark.regression
# 12) Validar la obtención de proyectos con diferentes configuraciones de filtro
def test_projects_with_filters():
    filters = {
        "color": "charcoal"
    }
    response = get_all_projects(get_token())
    assert_status_code(response, 200)
    assert_list(response)
    assert_filtro(response,filters)


