# encoding=utf-8
# Author: onlymyflower
# Date: 2018.4.29

# The codes do something that disobey FBI warning
# so be carefull
# if it occurs site unreachable error, open your VPN, set global proxy

import requests
from bs4 import BeautifulSoup
import urllib
import requests
import os
import time
# from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import argparse
import sys

DEF_DEBUG = 0
THREAD_NUM = 16

EXAMPLE_URLS = ["https://e-hentai.org/g/1218568/aa645c1938/",
"https://e-hentai.org/g/1186974/3811656035/",]

TMP_PATH = os.getcwd() + '/' + 'tmp'
os.makedirs(TMP_PATH, exist_ok=True)

# url_count = 1


def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

test_filename = 'test.html'

# save a set of images to a default path
def deal_with_sub_div(sub_div, save_path = TMP_PATH):
    sub_img_a = sub_div.find("a", recursive=True)
    sub_img_url = sub_img_a['href']
    sub_html = download_page(sub_img_url).decode('utf-8')
    sub_soup = BeautifulSoup(sub_html,"lxml")
    img = sub_soup.find("img", {"id": "img"}, recursive=True)
    img_url = img["src"]
    img_get = requests.get(img_url)
    image_name = os.path.split(img_url)[1]
    with open(save_path + '/' + image_name, "wb") as f:
        f.write(img_get.content)

def deal_with_url(url):
    
    # make the Pool of workers
    thread_num = 2

    html_doc = download_page(url).decode('utf-8')
    soup = BeautifulSoup(html_doc,"lxml")
    # with open("debug.html", "w") as f:
        # f.write(html_doc)
    # find elements by id
    img_table = soup.find("div", {"id": 'gdt'})
    #retuimg_div_list = img_table.find_all("div", {"class": 'gdtm'})
    img_div_list = img_table.find_all("div", {"class": "gdtm"})
    return img_div_list
    # print(len(img_div_list))
    # tasks = [(img_div, save_path) for img_div in img_div_list for save_path in save_path_dup]

    # print(tasks)
    # input("Press Enter to continue ...")

    # if thread_num < len(img_div_list):
        # thread_num = len(img_div_list)
    # pool = Pool(thread_num)
    # pool.map(deal_with_sub_div, tasks)
    # pool.close()
    

def main():
    sys.setrecursionlimit(2000)
    parser = argparse.ArgumentParser(description='TODO with more options')
    parser.add_argument(dest='urls',metavar='urls', nargs='*', default=EXAMPLE_URLS)
    args = parser.parse_args()
    print(args.urls)
    url_count = 0
    for url in args.urls:
        img_div_list = deal_with_url(url)
        save_path = TMP_PATH + '/' + str(url_count)
        os.makedirs(save_path, exist_ok=True)
        for sub_div in img_div_list:
            print("download url starts at:")
            print(time.asctime())
            deal_with_sub_div(sub_div, save_path)
            print("download url ends at:")
            print(time.asctime())
        url_count += 1

if __name__ == '__main__':
    main()