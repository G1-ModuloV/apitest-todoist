import pytest
from src.assertions.sections.delete_a_section_assertions import assert_status_code, assert_response_empty, \
    assert_section_exists, assert_error_message
from src.utils.section import delete_a_section


# TD-48 Verificar respuesta exitosa al eliminar una sección con un ID válido
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_section_with_valid_id(valid_token, valid_project_id, setup_create_a_section):
    section_id = setup_create_a_section
    response = delete_a_section(valid_token, section_id)
    assert_status_code(response, 204)
    assert_response_empty(response)


# TD-48 Verificar que la sección especificada por section_id existe antes de la eliminación
@pytest.mark.regression
def test_verify_section_exists_before_deletion(valid_token, valid_project_id, setup_create_a_section):
    section_id = setup_create_a_section
    assert_section_exists(section_id, valid_token)
    response = delete_a_section(valid_token, section_id)
    assert_status_code(response, 204)


# TD-48 Intentar eliminar una sección inexistente y confirmar que la respuesta es un estado 204 Not Found
@pytest.mark.regression
def test_delete_nonexistent_section(valid_token, nonexistent_section_id):
    response = delete_a_section(valid_token, nonexistent_section_id)
    assert_status_code(response, 204)


# TD-48 Verificar respuesta con token de autorización inválido
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_section_with_invalid_token(valid_project_id, setup_create_a_section,invalid_token):
    section_id = setup_create_a_section
    response = delete_a_section(invalid_token, section_id)
    assert_error_message(response, 401)


# TD-48 Verificar respuesta con token de autorización expirado
@pytest.mark.regression
def test_delete_section_with_expired_token(valid_project_id, setup_create_a_section, expired_token):
    section_id = setup_create_a_section
    response = delete_a_section(expired_token, section_id)
    assert_error_message(response, 401)


# TD-48 Verificar respuesta sin token de autorización
@pytest.mark.smoke
def test_delete_section_without_token(no_token, valid_project_id):
    response = delete_a_section(no_token, valid_project_id)
    assert_error_message(response, 401)



