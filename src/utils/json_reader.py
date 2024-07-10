import json
import os


def read_a_json(doc_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(current_dir, "..", "resources", "schemas", doc_name)
    with open(schema_path, "r") as content:
        mydata = json.load(content)
    return mydata
