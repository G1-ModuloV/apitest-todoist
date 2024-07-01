import json
from src.login import get_token
from src.utils.label import update_a_label
from src.resources.payloads.update_label_data import label_id, label_data
from src.assertions.labels.update_a_label_assertions import assert_update_a_label_case_one


def test_update_a_label():
    response = update_a_label(label_id, json.dumps(label_data), get_token())
    assert_update_a_label_case_one(response, label_data)

