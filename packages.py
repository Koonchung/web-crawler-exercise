import requests
import json
from bs4 import BeautifulSoup

url_main = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text='  
url_info = 'http://www.kuaidi100.com/query?type='


class kuaidi():
    def __init__(self):
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'www.kuaidi100.com',
            'Origin': 'http://www.kuaidi100.com',
            'Referer': 'http://www.kuaidi100.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.session = requests.Session()
        self.session.headers.update(headers)

    def package(self):
        self.num = input("请输入快递单号:")
        self.param = {
            'resultv2': '1',
            'text': self.num
        }
        # print(self.param)
        try:
            resp1 = self.session.post(url_main+self.num, params=self.param)
            soup = BeautifulSoup(resp1.content, "html.parser")
            # print(soup.prettify())
            jsondata = json.loads(soup.get_text())
            self.comcode = jsondata['auto'][0]['comCode']
            # print(self.comcode)
            resp2 = self.session.get(url_info+self.comcode+'&postid='+self.num)
            info = BeautifulSoup(resp2.content, "html.parser")
            # print(info.prettify())
            packagedata = json.loads(info.get_text())
            packageinfo = packagedata['data']
            # print(packageinfo)
            print(packageinfo[0]['time'],packageinfo[0]['context'])
            '''for each in packageinfo:
                print(each['time'], each['context'])'''
        except:
            print("Error.")


if __name__ == '__main__':
    while(True):
        kd = kuaidi()
        kd.package()
