# -*- coding: utf-8 -*-
# author: Chan

import requests
from bs4 import BeautifulSoup
import re
import codecs

url_main = 'http://dict.cn/dir/'
url_5_ = []
for i in range(0, 4):
    url_5_.append('http://dict.cn/dir/base5-' + str(i) + '.html')


class DICT(object):
    def __init__(self):
        headers = {
            'Referer': 'http://dict.cn/dir/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(headers)

    def words(self):
        self.word = []
        self.url_words = []
        for i in range(0, 4):
            resp_w = self.session.get(url_5_[i])
            soup_w = BeautifulSoup(resp_w.content, "html.parser")
            # print(soup.prettify())
            allwords = soup_w.find_all("a", {"target": "_blank"})
            pattern_words = re.compile(r'[A-Za-z]+')
            for i in range(0, len(allwords)):
                words = pattern_words.findall(allwords[i].text)
                # print(words)
                for i in range(0, len(words)):
                    self.word.append(words[0])
                    # print(self.word)
                    self.url_words.append('http://dict.cn/' + words[0])
                    # return self.url_words
                    #print (self.url_words)
        # print(len(self.url_words))
        # print(self.url_words)

    def trans(self):
        self.vocal = []
        self.mean=[]
        for i in range(0, len(self.url_words)):
            resp_t = self.session.get(self.url_words[i])
            soup_t = BeautifulSoup(resp_t.content, "html.parser")
            translation = soup_t.find_all("ul", {"class": "dict-basic-ul"})
            try:
                vocalulary = translation[0].find_all("span")           
                for i in range(0, len(vocalulary)):
                    vocals = vocalulary[i].text.strip()
                    self.vocal.append(vocals)
                    meaning = translation[0].find_all("strong")
                    for i in range(0, len(meaning)):
                        means = meaning[i].text.strip()
                        self.mean.append(means)
                        print(vocals, means)
            except:
                pass
                    

    def saveinfo(self):
        #info=[]
        name='D:/Download/English_words.txt'
        f=codecs.open(name,'w')
        for i in self.word:          
            f.write(str(i)+'\n')
        f.close()
        print("Words saved.")


if __name__ == '__main__':
    dir = DICT()
    dir.words()
    #dir.trans()
    dir.saveinfo()
