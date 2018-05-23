# -*- coding: utf-8 -*-
# Author: ElvinChan
# Date: 2018.3.15

import requests
from bs4 import BeautifulSoup


class Amazon_books(object):
    def scrap(self):
        url = 'https://www.amazon.cn/gp/bestsellers/digital-text/116169071?pf_rd_m=A1AJ19PSB66TGU&pageType=STOREFRONT&pf_rd_p=a9daf85d-aa24-446a-a1ca-2b67ade1a65b&pf_rd_r=HT0D10WVFSB96SF04BXC&pd_rd_wg=xNXr0&pf_rd_s=merchandised-search-3&pf_rd_t=40901&ref_=dbs_f_r_shv_ts_a9daf85d-aa24-446a-a1ca-2b67ade1a65b&pd_rd_w=cfaky&pf_rd_i=116169071&pd_rd_r=c970455b-f7cc-4146-9c06-d4cfd9674d76'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        container = soup.find_all("div", {"class": "zg_itemRow"})
        for contain in container:
            try:
                self.title = contain.find_all(
                    "a", {"class": "a-link-normal"})  # get the title of books
                # print(title[1].text.strip())
            except:
                pass
            self.author = contain.find_all(
                "span", {"class": "a-size-small a-color-base"})  # get authors
            # print(author[0].text)
            self.price = contain.find_all(
                "span", {"class": "a-size-base a-color-price"})  # get price
            # print(price[0].text)
            try:
                self.star = contain.find_all(
                    "i", {"class": "a-icon a-icon-star a-star-4-5"})  # get star
                # print(star[0].text)
            except:
                pass
            try:
                print("书名：", self.title[1].text.strip(), "\n作者：", self.author[0].text,
                      "\n价格：", self.price[0].text, "\n评价：", self.star[0].text, "\n")
            except:
                pass


if __name__ == '__main__':
    book = Amazon_books()
    book.scrap()
