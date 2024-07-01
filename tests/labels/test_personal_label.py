from src.login import get_token
from src.utils.label import get_a_personal_label
from src.assertions.labels.get_a_personal_label_assertions import (assert_get_personal_label_valid_case,
assert_get_personal_label_case_invalid_token, assert_get_personal_label_case_correct_date,
assert_get_personal_label_case_not_found)



#1 Verificar respuesta exitosa con un ID valido y un token de autenticación válido
def test_get_personal_label_valid_case():
    response = get_a_personal_label("2173775788", get_token())
    assert_get_personal_label_valid_case(response)

#2 Verificar respuesta de error 401 con un ID valido y un token invalido
def get_personal_label_case_invalid_token():
    response = get_a_personal_label("2173775788", "ec89cb82258d5f39de31b4850fa1505b214e25")
    assert_get_personal_label_case_invalid_token(response)


#3 Verificar respuesta correcta de campos esperados
def get_personal_label_case_correct_date():
    response = get_a_personal_label("2173775788", get_token())
    assert_get_personal_label_case_correct_date(response, "2173775788")

#4 Verificar respuesta de error 404 con un ID invalido y un token de autenticación válido
def assert_get_personal_label_case_not_found():
    response = get_a_personal_label("217377578", get_token())
    assert_get_personal_label_case_not_found(response)


#5 Verificar respuesta correcta de campos esperados en query param
def get_personal_label_case_query_param_correct_date():
    response = get_a_personal_label("?id=2173775788?id", get_token())
    assert_get_personal_label_case_correct_date(response, "2173775788")