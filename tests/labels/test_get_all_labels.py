from src.login import get_token
from src.utils.label import get_all_labels
from src.assertions.labels.get_all_labels_assertions import assert_get_all_labels_case_one


def test_get_all_labels():
    response = get_all_labels(get_token())
    assert_get_all_labels_case_one(response)
