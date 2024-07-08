project_data = {
    "valid_name": {"name": "Test Project"},
    "missing_name": {},
    "with_parent_id": {"name": "Test Project", "parent_id": "some_valid_parent_id"},
    "with_color": {"name": "Test Project", "color": "red"},
    "with_is_favorite": {"name": "Test Project", "is_favorite": True},
    "with_view_style": {"name": "Test Project", "view_style": "board"}
}

invalid_data = {
    "invalid_color": {"name": "Test Project", "color": "invalid_color"},
    "invalid_is_favorite": {"name": "Test Project", "is_favorite": "invalid_bool"},
    "invalid_view_style": {"name": "Test Project", "view_style": "invalid_view"}
}


def get_project_data(key):
    return project_data.get(key)


def get_invalid_data(key):
    return invalid_data.get(key)
