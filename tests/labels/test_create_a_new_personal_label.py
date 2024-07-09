import pytest
import json
from src.utils.label import (create_a_personal_label, delete_a_label,get_create_a_personal_label)
from src.resources.payloads.create_label_data import label_name, label_data, label_data2, empyte_data, invalid_data
from src.assertions.labels.create_a_new_personal_label_assertion import (assert_post_create_a_personal_label_name_valid,
                                                                         assert_post_create_a_personal_label_invalid_token,
                                                                         assert_post_create_a_personal_label_invalid_data,
                                                                         assert_get_create_a_personal_label)
from src.login import get_token


@pytest.mark.smoke
@pytest.mark.regression
# TD-24 Crea una etiqueta con un nombre valido
def test_create_a_personal_label_valid_name():
    response = create_a_personal_label(json.dumps(label_name), get_token())
    assert_post_create_a_personal_label_name_valid (response)
    label_id = response.json()["id"]
    delete_a_label(label_id, get_token())


@pytest.mark.smoke
@pytest.mark.regression
# TD-24 Crea una etiqueta con nombre y datos opcionales
def test_create_a_personal_label_all_valid():
   response = create_a_personal_label(json.dumps(label_data), get_token())
   assert_post_create_a_personal_label_name_valid(response)
   label_id = response.json()["id"]
   delete_a_label(label_id, get_token())


@pytest.mark.smoke
@pytest.mark.regression
# TD-24 Crea una etiqueta con un nombre y marcado como favorito
def test_create_a_personal_label_isFavorite():
   response = create_a_personal_label(json.dumps(label_data2), get_token())
   assert_post_create_a_personal_label_name_valid(response)
   label_id = response.json()["id"]
   delete_a_label(label_id, get_token())


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear un label con un token invalido 401
def test_create_a_personal_label_invalid_tokem(invalid_token):
   response = create_a_personal_label(json.dumps(label_data), invalid_token)
   assert_post_create_a_personal_label_invalid_token(response)


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear un label con un token vacio 401
def test_create_a_personal_label_invalid_tokem(no_token):
   response = create_a_personal_label(json.dumps(label_data), no_token)
   assert_post_create_a_personal_label_invalid_token(response)


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear un label con un formato de cuerpo incorrecto 400
def test_create_a_personal_label_invalid_data_body(valid_token):
   response = create_a_personal_label(json.dumps(invalid_data), valid_token)
   assert_post_create_a_personal_label_invalid_data(response)


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear un label con un formato de cuerpo vacio 400
def test_create_a_personal_label_invalid_data_body(valid_token):
   response = create_a_personal_label(json.dumps(empyte_data), valid_token)
   assert_post_create_a_personal_label_invalid_data(response)


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear con un verbo incorrecto error 403
def test_get_create_a_personal_label(valid_token):
   response = get_create_a_personal_label(json.dumps(empyte_data), valid_token)
   assert_get_create_a_personal_label(response)
