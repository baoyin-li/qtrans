from hashlib import md5

import requests


def trans(paragraph):
    api_url = 'http://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8&sl=auto&tl=zh_TW&q='
    api_url = api_url + paragraph
    response: requests.Response = requests.get(api_url)
    if response.status_code == 200:
        print(response.text)


def trans_from_baidu(paragraph):
    salt = '1435660288'
    appid= '20210918000949257'
    secret = 'XFXZB2ehSqaCKHZ7sabw'
    plain = f'{appid}{paragraph}{salt}{secret}'
    sign = md5(plain.encode()).hexdigest()
    url = f'http://api.fanyi.baidu.com/api/trans/vip/translate?q={paragraph}&from=en&to=zh&appid={appid}&salt={salt}&sign={sign}'
    response: requests.Response = requests.get(url)
    new_paragraphs = []
    if response.status_code == 200:
        json: dict = response.json()
        if 'trans_result' in json.keys():
            for item in json.get('trans_result'):
                print(item.get('dst'))
                new_paragraphs.append(item.get('dst'))

    return '\n'.join(new_paragraphs)
# paragraph = 'Rust is a programming language created by Graydon Hoare while working at Mozilla Research. He first started working on it around 2006 as a personal project, and by 2010 Mozilla had sponsored and announced the project. While the language is relatively new, it has quickly earned a passionate following of programmers who claim to even love using it.'
# trans_from_baidu(paragraph)
