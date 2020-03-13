# -*- coding:utf-8 -*-
import urllib2, sys

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return

        # 构建代理Handler
        httpproxy_handler = urllib2.ProxyHandler({"http" : "127.0.0.1:1087"})
        opener = urllib2.build_opener(httpproxy_handler)

        # 模拟浏览器可以加快爬取速度
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36')

        # response = urllib2.urlopen(req, timeout = 5)
        response = opener.open(req)

        #response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None
        else:
            return response.read()
