import pytest
import allure
from project_api_memes.conftest import negative_data_post
from project_api_memes.conftest import data1
from project_api_memes.conftest import negative_data_put


@allure.feature("GET /meme")
@allure.title("Получить все мемы — успешный ответ 200")
def test_get_all_memes_200(check_all_memes):
    check_all_memes.get_all_memes()
    check_all_memes.check_status_code(200)


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
def test_delete_memes_200(delete_one_memes, create_mem):
    delete_one_memes.delete_memes(create_mem)
    delete_one_memes.check_status_code(200)


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
