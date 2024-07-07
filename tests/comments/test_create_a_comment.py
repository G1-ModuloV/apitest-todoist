import pytest
from src.utils.comment import get_a_comment
from src.assertions.comments.get_a_comment_assertion import assert_get_a_comment_success


@pytest.mark.smoke
#Verificar que el request retorna crea un comentario valido
def test_create_a_comment(valid_token, setup_and_teardown_create_comment):
    commentID = setup_and_teardown_create_comment
    print("aca el valor de id json: ", commentID)

    response = get_a_comment(valid_token, commentID)
    assert_get_a_comment_success(response, commentID)
