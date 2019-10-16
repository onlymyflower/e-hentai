# encoding=utf-8
# Author: onlymyflower
# Date: 2018.4.29

# The codes do something that disobey FBI warning
# so be carefull
# if it occurs site unreachable error, open your VPN, set global proxy

from download_page import download_page

import requests
from bs4 import BeautifulSoup
import urllib
import requests
import os
import time
from multiprocessing.dummy import Pool as ThreadPool

DEF_DEBUG = 0
THREAD_NUM = 16

benzi_url = 'https://e-hentai.org/g/1186974/3811656035/' # kiara hotsprint event

# def download_page(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
#     }
#     data = requests.get(url, headers=headers).content
#     return data

test_filename = 'test.html'

def deal_with_sub_div(sub_div):
    sub_img_a = sub_div.find("a", recursive=True)
    sub_img_url = sub_img_a['href']
    sub_html = download_page(sub_img_url).decode('utf-8')
    sub_soup = BeautifulSoup(sub_html,"lxml")
    img = sub_soup.find("img", {"id": "img"}, recursive=True)
    img_url = img["src"]
    img_get = requests.get(img_url)
    image_name = os.path.split(img_url)[1]
    with open(image_name, "wb") as f:
        f.write(img_get.content)


def main():
    print("program starts at:")
    print(time.asctime())

    # make the Pool of workers
    pool = ThreadPool(THREAD_NUM)

    html_doc = download_page(benzi_url).decode('utf-8')
    soup = BeautifulSoup(html_doc,"lxml")
    # find elements by id
    img_table = soup.find("div", {"id": 'gdt'})
    img_div_list = img_table.find_all("div", {"class": 'gdtm'})

    results = pool.map(deal_with_sub_div, img_div_list)

    print("program ends at:")
    print(time.asctime())

if __name__ == '__main__':
    main()
