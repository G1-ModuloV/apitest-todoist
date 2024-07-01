
from src.login import get_token
from src.utils.comment import get_comment
from src.assertions.comments.get_a_comment_assertion import assert_get_get_a_comment_success

#1. Verificar que el request retorna el comentario seleccionado usando un codigo de autenticación valido
def test_a_comment():
    response = get_comment(get_token())
    assert_get_get_a_comment_success(response)

#2. Verificar que el request retorna un codigo de error usando un codigo de autenticación invalido
#3. Verificar que el retorna un codigo de error usando un codigo de autenticacion nulo/vacio
#4. Verificar que el request retorna un comentario especifico usando el id valido del comentario
#5. Verificar que el request retorna un codigo de error usando un id de comentario invalido
#6. Verificar que el request retorna un codigo de error usando el nulo/vacio del comentario