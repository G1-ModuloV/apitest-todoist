from config import BASE_URI


def label_url(label_id):
    return f"{BASE_URI}/rest/v2/labels/{label_id}"
