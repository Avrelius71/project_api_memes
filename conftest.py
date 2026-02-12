import pytest

from project_api_memes.method.get_all_memes import GetAllMemes
from project_api_memes.method.get_one_memes import GetOneMemes
from project_api_memes.method.delete_memes import DeleteMemes
from project_api_memes.method.post_meme import PostMemes
from project_api_memes.method.put_meme import PutMemes
from project_api_memes.method.post_aus import PostAus
from project_api_memes.method.get_token import GetToken


@pytest.fixture()
def check_all_memes():
    return GetAllMemes()


@pytest.fixture()
def check_one_memes():
    return GetOneMemes()


@pytest.fixture()
def delete_one_memes():
    return DeleteMemes()


@pytest.fixture()
def create_post_memes():
    return PostMemes()


@pytest.fixture()
def put_old_memes():
    return PutMemes()


@pytest.fixture()
def post_authorize():
    return PostAus()


@pytest.fixture()
def get_my_token():
    return GetToken()


@pytest.fixture()
def create_and_delete_mem(create_post_memes, delete_one_memes):
    payload = {'text': 'abra',
               'url': 'stoyatb',
               'tags': ['aqa6'],
               'info': {'project': 'api_test'}}
    create_post_memes.post_memes(payload)
    yield create_post_memes.json['id']
    delete_one_memes.delete_memes(create_and_delete_mem)


@pytest.fixture()
def create_mem(create_post_memes):
    payload = {'text': 'abra',
               'url': 'stoyatb',
               'tags': ['aqa6'],
               'info': {'project': 'api_test'}}
    create_post_memes.post_memes(payload)
    yield create_post_memes.json['id']


@pytest.fixture()
def put_payload(create_and_delete_mem):
    return {
        'id': create_and_delete_mem,
        'text': 'choto gdeto',
        'url': 'test_put',
        'tags': ['aqa4', 'aqa5', 'aqa6'],
        'info': {'lesson3': 'chay', 'lesson4': 'kofe'}
    }


@pytest.fixture()
def create_token(post_authorize):
    payload = {'name': 'Artem'}
    post_authorize.post_aus(payload)
    token = post_authorize.json['token']
    yield token