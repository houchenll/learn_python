# -*- coding:utf-8 -*-
import urllib2

# 若有data是post，若无data是get
# response是服务器响应的类文件对象
url = 'http://www.python.org/'
response = urllib2.urlopen(url)

# 服务器返回的类文件对象支持python文件对象的操作方法
# 如 read()读取文件全部内容，返回字符串
html = response.read()

print(html)
