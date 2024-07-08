label_id = "2173805399"
incorrect_label_id = "48596"
label_data = {"name": "important"}
label_data2 = {"name": "Prueba2"}
correct_payload = [label_data, {"order": 1}, {"color": "red"}, {"is_favorite": True},
                   {"name": "etiqueta 15", "order": 1, "color": "red", "is_favorite": True}]
bad_payload = [{}, {"order": False}, {"is_favorite": False}]
bad_argument = [{"name": True}, {"name": 15}, {"order": "uno"}]
bad_color = [{"color": True}, {"color": 15}, {"color": "pink"}]
