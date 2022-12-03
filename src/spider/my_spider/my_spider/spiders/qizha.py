import re
from urllib import parse

import scrapy


class QizhaSpider(scrapy.Spider):
    name = 'qizha'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E5%B8%9D&ie=utf-8']

    def parse(self, response):
        # print(response.text)
        # 页面中帖子的url地址
        url_list = response.css('.j_th_tit::attr(href)').extract()
        # print(url_list)

        # 解析url
        for url in url_list:
            print(url)
            yield scrapy.Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)

    def parse_detail(self, response):
        print(response.text)
        title = response.css('.core_title_txt.pull-left.text-overflow::text').extract()
        print(title)
        authors = response.css('.p_author_name.j_user_card::text').extract()
        print(authors)
        contents = response.css('.d_post_content.j_d_post_content').extract()
        print(contents)
        contents_list = self.get_content(contents)
        # 处理帖子发送时间和楼数
        sendtime_list, floor_list = self.get_send_time_and_floor(response)

    def get_content(self, contents):
        contents_list = []
        for content in contents:
            reg = ";\">(.*)</div>"
            result = re.findall(reg, content)[0]
            contents_list.append(result)
        return contents_list

    def get_send_time_and_floor(self, response):
        time_and_floor_list = response.css('.post-tail-wrap span[class=tail-info]::text').extract()
        i = 0
        time_list = []
        floor_list = []
        for time_and_floor in time_and_floor_list:
            if i % 2 == 0:
                floor_list.append(time_and_floor)
            elif i % 2 == 1:
                time_list.append(time_and_floor)
            i += 1
        return time_list, floor_list
