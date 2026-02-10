import pytest

from project_api_memes.method.get_all_memes import GetAllMemes
from project_api_memes.method.get_one_memes import GetOneMemes
from project_api_memes.method.delete_memes import DeleteMemes
from project_api_memes.method.post_meme import PostMemes
from project_api_memes.method.put_meme import PutMemes


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


negative_data_post = [
    {'url': 'stoyatb', 'tags': ['aqa1'], 'info': {'test': 'odin'}},
    {'text': 'testim choto', 'tags': ['aqa1'], 'info': {'test': 'odin'}},
    {'text': 'testim choto', 'url': 'stoyatb', 'info': {'test': 'odin'}},
    {'text': 'testim choto', 'url': 'stoyatb', 'tags': ['aqa1']},
    {'url': 1234, 'text': 'testim choto', 'tags': ['aqa1'], 'info': {'test': 'odin'}},
    {'url': 'stoyatb', 'text': 1234, 'tags': ['aqa1'], 'info': {'test': 'odin'}},
    {'url': 'stoyatb', 'text': 'testim choto', 'tags': 1234, 'info': {'test': 'odin'}},
    {'url': 'stoyatb', 'text': 'testim choto', 'tags': ['aqa1'], 'info': 1234},
    {'url': 'stoyatb', 'text': 'testim choto', 'tags': ['aqa1'], 'info': 'sdaf'},
    {'url': 'stoyatb', 'text': 'testim choto', 'tags': 'asdf', 'info': {'test': 'odin'}},
]

data1 = {'text': 'testim choto',
         'url': 'stoyatb',
         'tags': ['aqa1', 'aqa2', 'aqa3'],
         'info': {'lesson1': 'pytest', 'lesson2': 'paycharm'}}

negative_data_put = [
    {'text': 'testim choto', 'tags': ['aqa'], 'info': {'lesson': 'tea'}},
    {'url': 'test', 'tags': ['aqa'], 'info': {'lesson': 'tea'}},
    {'url': 'test', 'text': 'testim choto', 'info': {'lesson': 'tea'}},
    {'url': 'test', 'text': 'testim choto', 'tags': ['aqa']},
    {'url': 1234, 'text': 'testim choto', 'tags': ['aqa'], 'info': {'lesson': 'tea'}},
    {'url': 'test', 'text': 1234, 'tags': ['aqa'], 'info': {'lesson': 'tea'}},
    {'url': 'test', 'text': 'testim choto', 'tags': 1234, 'info': {'lesson': 'tea'}},
    {'url': 'test', 'text': 'testim choto', 'tags': ['aqa'], 'info': 1234},
    {'url': 'test', 'text': 'testim choto', 'tags': 'asdf', 'info': {'lesson': 'tea'}},
    {'url': 'test', 'text': 'testim choto', 'tags': ['aqa'], 'info': 'asdf'}
]