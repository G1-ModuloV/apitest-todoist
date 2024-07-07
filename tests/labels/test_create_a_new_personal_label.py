import pytest
import json
from src.utils.label import create_a_personal_label, delete_a_label
from src.resources.payloads.create_label_data import label_name,label_data, label_data2
from src.assertions.labels.create_a_new_personal_label_assertion import assert_post_create_a_personal_label_name_valid
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