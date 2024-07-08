import pytest
from src.utils.project import delete_a_project, get_a_project
from src.assertions.projects.delete_a_project_assertions import assert_status_code, assert_empty_data, assert_name_no_exist


@pytest.mark.smoke
@pytest.mark.regression
# TD-6 Verificar eliminación exitosa de un proyecto existente
def test_successful_project_deletion(valid_token, setup_delete_project):
    project_id = setup_delete_project
    response = delete_a_project(valid_token, project_id)
    assert_status_code(response, 204)
    assert_empty_data(response)
    response = get_a_project(valid_token, project_id)
    assert_name_no_exist(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-6 Validar respuesta con token de autorización inválido
def test_invalid_token(setup_delete_project, invalid_token):
    project_id = setup_delete_project
    response = delete_a_project(invalid_token, project_id)
    assert_status_code(response, 401)


@pytest.mark.smoke
@pytest.mark.regression
# TD-6 Verificar respuesta sin token
def test_no_token(setup_delete_project, no_token):
    project_id = setup_delete_project
    response = delete_a_project(no_token, project_id)
    assert_status_code(response, 401)


@pytest.mark.regression
# TD-6 Validar respuesta para un ID de proyecto no existente
def test_nonexistent_project(nonexistent_project_id, valid_token):
    response = delete_a_project(valid_token, nonexistent_project_id)
    assert_status_code(response, 204)


@pytest.mark.regression
# TD-6 Verificar que un proyecto eliminado no tenga acceso posterior
def test_deleted_project_access(valid_token, setup_delete_project):
    project_id = setup_delete_project
    response = delete_a_project(valid_token, project_id)
    assert_status_code(response, 204)
    assert_empty_data(response)
    response = get_a_project(valid_token, project_id)
    assert_status_code(response, 404)
