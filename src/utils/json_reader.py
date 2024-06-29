import json


def read_a_json(doc_name):
    with open(f"./../src/resources/schemas/{doc_name}", "r") as content:
        mydata = json.load(content)
    return mydata
