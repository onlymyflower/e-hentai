# encoding=utf-8
# Author: onlymyflower
# Date: May 10, 2018

from download_page import download_page
import requests
from bs4 import BeautifulSoup
import urllib
import requests
import os
import time
# from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing.dummy import Pool as ThreadPool
import argparse
import sys
import logging

# @paras
# rootpath, sourceUrl, coverUrl, other info

# os.environ['HOME']
# rootpath=os.environ['HOME'] + "/" +"tmp"

# save a set of images to a default path


def deal_with_sub_div(sub_div, rootpath=os.environ['HOME'] + "/" + "tmp"):
    sub_img_a = sub_div.find("a", recursive=True)
    sub_img_url = sub_img_a['href']
    sub_html = download_page(sub_img_url).decode('utf-8')
    sub_soup = BeautifulSoup(sub_html, "lxml")
    img = sub_soup.find("img", {"id": "img"}, recursive=True)
    img_url = img["src"]
    print(img_url)
    img_get = requests.get(img_url)
    image_name = os.path.split(img_url)[1]
    print(image_name)
    with open(rootpath + '/' + image_name, "wb") as f:
        f.write(img_get.content)
        print("saved to: " + rootpath + '/' + image_name)

<<<<<<< HEAD:download_benzi.py
def deal_with_url(url):
    html_doc = download_page(url).decode('utf-8')
    soup = BeautifulSoup(html_doc,"lxml")
    # find elements by id
    img_table = soup.find("div", {"id": "gdt"})
    try:
        assert img_table != None
    except AssertionError:
        logging.error("img_table is None, maybe encountered warning window", exc_info=True)
        with open("warning.html","w") as f:
            print(html_doc,file=f)
        # program won't exit
        # keep tackle that
        # https://e-hentai.org/g/1192266/8f3bc71342/?nw=session
        # https://e-hentai.org/g/1192266/8f3bc71342/?nw=always
        new_url = url + "/" + "?nw=session"
        return deal_with_url(new_url) # recursive?


    img_div_list = img_table.find_all("div", {"class": "gdtm"})
    return img_div_list
=======
>>>>>>> 0861feb... update code to rebuild for e-hentai:e-hentai/download_benzi.py

# download single benzi


def download_benzi(sourceUrl="https://e-hentai.org/g/1178073/30bc24b00a/", benzi_store_path=os.environ['HOME'] + "/" + "tmp"):

    print("Starts downloading at:")
    print(time.asctime())

    os.makedirs(benzi_store_path, exist_ok=True)

    print("downloading: " + sourceUrl)

    img_div_list = deal_with_url(sourceUrl)

    for sub_div in img_div_list:
        deal_with_sub_div(sub_div, benzi_store_path)

    print("Finishes downloading at:")
    print(time.asctime())
