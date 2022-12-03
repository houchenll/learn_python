# -*- coding:utf-8 -*-

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, datas):
        if datas is None:
            print 'new datas is none'
            return

        for data in datas:
            self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write('<html>')

        # 需要指定网页编码，否则打开网页看到的中文是乱码
        fout.write('<head>')
        fout.write('<meta charset="UTF-8">')
        fout.write('</head>')

        fout.write('<body>')

        # python default encoding is ascii
        # <a href="http://www.w3school.com.cn">W3School</a>
        for data in self.datas:
            fout.write('<p>')
            fout.write('<a href="')
            fout.write(data['url'])
            fout.write('">')
            fout.write(data['title'].encode('UTF-8'))
            fout.write('</a>')
            fout.write('</p>')

        fout.write('</body>')
        fout.write('</html>')

        fout.close()
