# -*- coding:utf-8 -*-
import json
from zhconv import convert


def paragraphs_to_content(paras):
    result = ''
    for para in paras:
        result = result + para + u'\n'
    while result.endswith(u'\n'):
        result = result[:-1]
    return result


# path = '/Users/ll/poem/github/chinese-poetry/json/poet.tang.0.json'
# f = open(path, 'r')
# text = f.read()
# poem_list = json.loads(text)
# for poem in poem_list:
#     paragraphs = poem['paragraphs']
#     tradition_content = paragraphs_to_content(paragraphs)
#     # print('tradition content', content)
#     print(tradition_content)
#     simple_content = convert(tradition_content, 'zh-cn')
#     print(simple_content)

path = '/Users/ll/code/workspace/python/zh/error.text.json'
f = open(path, 'r')
tradition_text = f.read()
print(tradition_text)
# simple_text = convert(tradition_text, 'zh-hans')
simple_text = convert(tradition_text, 'zh-cn')
print(simple_text)
