label_name = {"name": "test rest"}
label_data = {"name": "Manual testing", "color": "red", "is_favorite": True}
label_data2 = {"name": "Automation test", "is_favorite": True}
invalid_name = {"name": "no exist"}
invalid_data = {"color": "red", "is_favorite": True}
empty_data = {}

label_payload2 = {"name": "Core testing"}
task_payload2 = {
    "content": "new task shared label",
}
updated_task_payload2 = {
    "labels": [label_payload2["name"]],
}
