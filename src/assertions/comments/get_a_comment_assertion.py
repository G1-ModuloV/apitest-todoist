from src.utils.comment import get_a_comment
from src.utils.json_reader import read_a_json
from src.assertions.schema_assertion import assert_schema

#Verificar que el retorna un codigo de error usando un codigo de autenticacion nulo/vacio
def assert_get_a_comment_code_401(response):
    assert response.status_code == 401

#Verificar que el request retorna un comentario especifico usando el id valido del comentario
def assert_get_a_comment_success(response, valid_comment_id):
    schema = read_a_json("comment_schema.json")
    assert_schema(response, schema)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    response_json = response.json()
    assert response_json['id'] == valid_comment_id

#Verificar que el request retorna un codigo de error usando un id de comentario invalido
#Verificar que el request retorna un codigo de error usando el nulo/vacio del comentario
def assert_get_a_comment_code_400(response):
    assert response.status_code == 400