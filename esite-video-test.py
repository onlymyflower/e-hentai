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
from multiprocessing.dummy import Pool as ThreadPool

DEF_DEBUG = 0
THREAD_NUM = 16

video_url = 'https://video-hw.xvideos-cdn.com/videos/mp4/6/8/8/xvideos.com_68823d775dead9437264ee3bab92f2e8.mp4?e=1525115242&h=e848c52cbb674a05267c0019940e9a5d&download=1'


video_url = "https://video-hw.xvideos-cdn.com/videos/mp4/6/8/8/xvideos.com_68823d775dead9437264ee3bab92f2e8.mp4?e=1525131802&h=b06e662a81d5e80adac2450d77e27df7&download=1"
def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

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

    video_get = requests.get(video_url)
    video_name = os.path.split(video_url)[1]
    with open(video_name, "wb") as f:
        f.write(video_get.content)

    print("program ends at:")
    print(time.asctime())

if __name__ == '__main__':
    main()
