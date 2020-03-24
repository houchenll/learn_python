import urllib.request
import ssl

# 取消证书验证，避免报错
ssl._create_default_https_context = ssl._create_unverified_context

# Request是一个class
# urlopen默认的user-agent是Python-urllib/3.8，容易被服务器屏蔽，需要修改
# 构建请求报头对象，重构user-agent
url = "http://www.baidu.com/"
ua_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
request = urllib.request.Request(url, headers = ua_headers)

response = urllib.request.urlopen(request)

result = response.read(1000)

print(result)