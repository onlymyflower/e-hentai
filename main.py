# encoding=utf-8
# Author: onlymyflower
# Date: May 9, 2018

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
# from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import argparse
import sys

QUERY = "https://e-hentai.org/?f_doujinshi=on&f_manga=on&f_artistcg=on&f_gamecg=on&f_western=on&f_non-h=on&f_imageset=on&f_cosplay=on&f_asianporn=on&f_misc=on&f_search=%E3%82%86%E3%82%8B%E3%82%86%E3%82%8A&f_apply=Apply+Filter&inline_set=dm_t"
# "https://e-hentai.org/?f_doujinshi=on&f_manga=on&f_artistcg=on&f_gamecg=on&f_western=on&f_non-h=on&f_imageset=on&f_cosplay=on&f_asianporn=on&f_misc=on&f_search=%E3%82%86%E3%82%8B%E3%82%86%E3%82%8A&f_apply=Apply+Filter"
# get query

# ROOTPATH = os.getcwd()

query_result = download_page(QUERY).decode('utf-8')
root_soup = BeautifulSoup(query_result,"lxml")

thumbnails = root_soup.find_all("div", {"class", "id1"})
title = thumbnails[0].find("div", {"class", "id2"}) # title
cover = thumbnails[0].find("div", {"class", "id3"}) # cover
coverImg = cover.find("img")
coverUrl = coverImg["src"]
comments = thumbnails[0].find("div", {"class", "id4"}) # comments, todo
a = title.find("a") # (C87) [Suzume Holic (Ryamu, Fon)] Endless Relation (YuruYuri)
titleText = a.text
sourceUrl = a["href"]
print(sourceUrl)

# @paras
# rootpath, sourceUrl, coverUrl, other info

# os.environ['HOME']
# rootpath=os.environ['HOME'] + "/" +"tmp"

# save a set of images to a default path
def deal_with_sub_div(sub_div,rootpath=os.environ['HOME'] + "/" +"tmp"):
    sub_img_a = sub_div.find("a", recursive=True)
    sub_img_url = sub_img_a['href']
    sub_html = download_page(sub_img_url).decode('utf-8')
    sub_soup = BeautifulSoup(sub_html,"lxml")
    img = sub_soup.find("img", {"id": "img"}, recursive=True)
    img_url = img["src"]
    print(img_url)
    img_get = requests.get(img_url)
    image_name = os.path.split(img_url)[1]
    print(image_name)
    with open(rootpath + '/' + image_name, "wb") as f:
        f.write(img_get.content)
        print("saved to: " + rootpath + '/' + image_name)

def deal_with_url(url):
    html_doc = download_page(url).decode('utf-8')
    soup = BeautifulSoup(html_doc,"lxml")
    # find elements by id
    img_table = soup.find("div", {"id": 'gdt'})
    img_div_list = img_table.find_all("div", {"class": "gdtm"})
    return img_div_list

# download single benzi
def download_benzi(sourceUrl="https://e-hentai.org/g/1178073/30bc24b00a/",rootpath=os.environ['HOME'] + "/" +"tmp"):
    os.makedirs(rootpath, exist_ok=True)
    img_div_list = deal_with_url(sourceUrl)
    with open("debug.txt","w") as f:
        print(img_div_list,file=f)
    for sub_div in img_div_list:
        deal_with_sub_div(sub_div,os.getcwd())


def __main__():
    download_benzi()

if __name__ == '__main__':
    __main__()
# print(titleText)

# deal with single url with previous codes
# with open("log.txt","w") as f:
    # print(thumbnails, file=f)

# "cover" # dir
# "${title}" # dir
# "${query}" # dir in ROOTPATH

# os.makedirs(TMP_PATH, exist_ok=True)
# with open("query_result.html","w") as f:
    # print(query_result, file=f)

# get benzi links

# download single benzi
