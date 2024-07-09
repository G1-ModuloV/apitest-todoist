import pytest
import json
from src.utils.label import remove_a_shared_label, get_remove_a_shared_label
from src.resources.payloads.create_label_data import (label_name, invalid_name, invalid_data)
from src.assertions.labels.remove_shared_labels_assertion import  (assert_post_remove_a_shared_label,
                                                                   assert_post_remove_a_shared_label_invalid_token,
                                                                   assert_get_remove_a_shared_label,
                                                                   assert_remove_a_shared_label_invalid_body)


@pytest.mark.smoke
@pytest.mark.regression
# TD-49 verificar que se remueva una etiqueta compartida respuesta 204(no contain)
def test_remove_shared_label_valid(valid_token):
    response = remove_a_shared_label(json.dumps(label_name), valid_token)
    assert_post_remove_a_shared_label(response)
    print (response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-49 verificar la respuesta de remover una etiqueta compartida que no existe
def test_remove_shared_label_invalid_name(valid_token):
    response = remove_a_shared_label(json.dumps(invalid_name), valid_token)
    assert_post_remove_a_shared_label(response)
    print (response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-49 verificar la respuesta al ingresar un token invalido respuesta 401 (Unauthorized)
def test_remove_shared_label_invalid_token(invalid_token):
    response = remove_a_shared_label(json.dumps(label_name), invalid_token)
    assert_post_remove_a_shared_label_invalid_token(response)
    print (response)


@pytest.mark.regression
# TD-49 verificar la respuesta al ingresar un token vacio respuesta 401 (Unauthorized)
def test_remove_shared_label_sin_token(no_token):
    response = remove_a_shared_label(json.dumps(label_name),no_token)
    assert_post_remove_a_shared_label_invalid_token(response)
    print (response)


@pytest.mark.regression
# TD-49 verificar la respuesta al realizar la consulta con verbo incorrecto 403(bad request)
def test_get_remove_shared_label(valid_token):
    response = get_remove_a_shared_label(json.dumps(label_name), valid_token)
    assert_get_remove_a_shared_label(response)
    print (response)


@pytest.mark.regression
# TD-49 verificar la respuesta al poner el cuerpo en formato incorrecto 400 (bad request)
def test_remove_shared_label_invalid_body(valid_token):
    response = remove_a_shared_label(invalid_data,valid_token)
    assert_remove_a_shared_label_invalid_body(response)
    print (response)
