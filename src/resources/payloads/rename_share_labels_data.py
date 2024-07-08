label_payload = {"name": "my label"}
task_payload = {
    "content": "my new task",
}
updated_task_payload = {
        "labels": [label_payload["name"]],
}
payload_correct = {"name": "my label", "new_name": "renamed label"}
payload_good_new_name = [
    payload_correct,
    {"name": "my label", "new_name": 1234},
    {"name": "my label", "new_name": True}
]
payload_bad_name = [
    {"name": "nonexistent", "new_name": "renamed label"},
    {"name": 1234, "new_name": "renamed label"},
    {"name": True, "new_name": "renamed label"},
    {"new_name": "renamed label"}
]
payload_bad_new_name = [
    {"name": "my label", "new_name": ""},
    {"name": "my label"},
    {}
]
