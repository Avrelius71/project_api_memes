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

data_aus = {'name': 'Artem'}

data_aus_negative = [
    {'name': 1234},
    {}
]
