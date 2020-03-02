import requests


URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
KEY_API = 'trnsl.1.1.20190827T202940Z.2c49395d596e72e6.b347e4d8ce5e733c54bcbf89895db63e5841a947'


def translate(text):
    '''
    translation input text
    :return:
    translated text
    '''
    params = {
        'key': KEY_API,
        'text': text,
        'lang': 'en-ru',
    }
    response = requests.get(URL, params=params)
    return ''.join(response.json()['text'])