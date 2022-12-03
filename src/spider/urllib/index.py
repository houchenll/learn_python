import urllib.request

url = 'http://www.baidu.com/'
response = urllib.request.urlopen(url)

# 服务器返回的类文件对象支持python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串
result = response.read()
print(result)
