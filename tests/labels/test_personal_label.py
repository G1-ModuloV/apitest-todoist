import pytest
from src.utils.label import get_a_personal_label
from src.assertions.labels.get_a_personal_label_assertions import (assert_get_personal_label_valid_case,
                                                                   assert_get_personal_label_case_invalid_token,
                                                                   assert_get_personal_label_case_correct_date,
                                                                   assert_get_personal_label_case_not_found)


@pytest.mark.smoke
# TD-23 Verificar respuesta exitosa con un ID valido y un token de autenticación válido
def test_get_personal_label_valid_case(valid_label_id, valid_token):
    response = get_a_personal_label(valid_label_id, valid_token)
    assert_get_personal_label_valid_case(response)

@pytest.mark.regression
# TD-23 Verificar respuesta de error 401 con un ID valido y un token invalido
def test_get_personal_label_case_invalid_token(valid_label_id, invalid_token):
    response = get_a_personal_label(valid_label_id, invalid_token)
    assert_get_personal_label_case_invalid_token(response)


@pytest.mark.smoke
# TD-23 Verificar respuesta correcta de campos esperados
def test_get_personal_label_case_correct_date(valid_label_id, valid_token):
    response = get_a_personal_label(valid_label_id, valid_token)
    assert_get_personal_label_case_correct_date(response, valid_label_id)

@pytest.mark.regression
# TD-23 Verificar respuesta de error 404 con un ID invalido y un token de autenticación válido
def test_assert_get_personal_label_case_not_found(invalid_label_id, valid_token):
    response = get_a_personal_label(invalid_label_id, valid_token)
    assert_get_personal_label_case_not_found(response)

@pytest.mark.smoke
# TD-23 Verificar respuesta correcta de campos esperados en query param
def test_get_personal_label_case_query_param_correct_date(valid_query_param_label_id, valid_token):
    response = get_a_personal_label(valid_query_param_label_id, valid_token)
    assert_get_personal_label_case_correct_date(response, valid_query_param_label_id)

@pytest.mark.regression
# TD-23 Verificar respuesta de error 404 con un ID de un label eliminado y un token de autenticación válido
def test_get_delete_label_id_case_not_found(deleted_label_id, valid_token):
    response = get_a_personal_label(deleted_label_id, valid_token)
    assert_get_personal_label_case_not_found(response)