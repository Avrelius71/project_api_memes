import pytest
import allure
from project_api_memes.data import negative_data_post
from project_api_memes.data import data1
from project_api_memes.data import negative_data_put
from project_api_memes.data import data_aus
from project_api_memes.data import data_aus_negative


@allure.feature("GET /meme")
@allure.title("Получить все мемы — успешный ответ 200")
def test_get_all_memes_200(check_all_memes):
    check_all_memes.get_all_memes()
    check_all_memes.check_status_code(200)
    check_all_memes.check_json()


@allure.feature("GET /meme")
@allure.title("Получить все мемы без валидного токена — 401")
def test_get_all_memes_401(check_all_memes):
    check_all_memes.get_all_memes(headers={'Authorization': 'M'})
    check_all_memes.check_status_code(401)


@allure.feature("GET /meme/{id}")
@allure.title("Получить мем по существующему ID — 200")
def test_get_one_memes_200(check_one_memes, create_and_delete_mem):
    check_one_memes.get_one_memes(create_and_delete_mem)
    check_one_memes.check_status_code(200)
    check_one_memes.check_id(create_and_delete_mem)


@allure.feature("GET /meme/{id}")
@allure.title("Получить мем по несуществующему ID — 404")
def test_get_one_memes_404(check_one_memes):
    check_one_memes.get_one_memes("abc")
    check_one_memes.check_status_code(404)


@allure.feature("GET /meme/{id}")
@allure.title("Получить мем без валидного токена — 401")
def test_get_one_memes_401(check_one_memes, create_and_delete_mem):
    check_one_memes.get_one_memes(create_and_delete_mem, headers={'Authorization': 'M'})
    check_one_memes.check_status_code(401)


@allure.feature("DELETE /meme/{id}")
@allure.title("Удалить мем — успешный ответ 200")
def test_delete_memes_200(delete_one_memes, create_mem, check_one_memes):
    delete_one_memes.delete_memes(create_mem)
    delete_one_memes.check_status_code(200)
    check_one_memes.get_one_memes(create_mem)
    check_one_memes.check_status_code(404)


@allure.feature("DELETE /meme/{id}")
@allure.title("Удалить несуществующий мем — 404")
def test_delete_memes_404(delete_one_memes):
    fake_id = 999999999
    delete_one_memes.delete_memes(fake_id)
    delete_one_memes.check_status_code(404)


@allure.feature("DELETE /meme/{id}")
@allure.title("Удалить мем без валидного токена — 401")
def test_delete_memes_401(delete_one_memes, create_mem):
    delete_one_memes.delete_memes(create_mem, headers={'Authorization': 'M'})
    delete_one_memes.check_status_code(401)


@allure.feature("POST /meme")
@allure.title("Создать мем — успешный ответ 200")
def test_post_memes_200(create_post_memes):
    create_post_memes.post_memes(data1)
    create_post_memes.check_status_code(200)
    create_post_memes.check_response_body(data1)


@allure.feature("POST /meme")
@allure.title("Создать мем с некорректными данными — 400")
@pytest.mark.parametrize('data', negative_data_post)
def test_post_memes_400(create_post_memes, data):
    create_post_memes.post_memes(data)
    create_post_memes.check_status_code(400)


@allure.feature("POST /meme")
@allure.title("Создать мем без валидного токена — 401")
def test_post_memes_401(create_post_memes):
    create_post_memes.post_memes(data1, headers={'Authorization': 'M'})
    create_post_memes.check_status_code(401)


@allure.feature("PUT /meme/{id}")
@allure.title("Обновить мем — успешный ответ 200")
def test_put_memes_200(create_and_delete_mem, put_old_memes, put_payload):
    put_old_memes.put_memes(create_and_delete_mem, put_payload)
    put_old_memes.check_status_code(200)
    put_old_memes.check_response_body(put_payload, create_and_delete_mem)


@allure.feature("PUT /meme/{id}")
@allure.title("Обновить мем с некорректными данными — 400")
@pytest.mark.parametrize('data', negative_data_put)
def test_put_memes_400(create_and_delete_mem, put_old_memes, data):
    put_old_memes.put_memes(create_and_delete_mem, data)
    put_old_memes.check_status_code(400)


@allure.feature("PUT /meme/{id}")
@allure.title("Обновить мем без валидного токена — 401")
def test_put_memes_401(create_and_delete_mem, put_old_memes, put_payload):
    put_old_memes.put_memes(create_and_delete_mem, put_payload, headers={'Authorization': 'M'})
    put_old_memes.check_status_code(401)


@allure.feature("POST /authorize")
@allure.title("Проверяем авторизацию — 200")
def test_post_aus_200(post_authorize):
    post_authorize.post_aus(data_aus)
    post_authorize.check_status_code(200)
    post_authorize.check_name()


@allure.feature("POST /authorize")
@allure.title("Проверяем невалидные данные - 400")
@pytest.mark.parametrize('data', data_aus_negative)
def test_post_aus_400(post_authorize, data):
    post_authorize.post_aus(data)
    post_authorize.check_status_code(400)


@allure.feature("GET /authorize/{token}")
@allure.title("Проверить жив ли токен - 200")
def test_get_token_200(get_my_token, create_token):
    get_my_token.get_token(create_token)
    get_my_token.check_status_code(200)


@allure.feature("GET /authorize/{token}")
@allure.title("Проверить несуществующий токен - 404")
def test_get_token_404(get_my_token):
    get_my_token.get_token("asdf")
    get_my_token.check_status_code(404)
