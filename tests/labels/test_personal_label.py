import pytest
import jsonschema

from src.login import get_token
from src.utils.label import get_a_personal_label
from src.assertions.labels.get_a_personal_assertions import assert_get_personal_label_case_one


def test_get_personal_label():
    response = get_a_personal_label(get_token())
    assert_get_personal_label_case_one(response)