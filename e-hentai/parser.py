#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Sep-30-19 16:49
# @Author  : onlymyflower
# @Link    : http://example.org

import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from utils import download_page


def doujinshi_parser(url):
    '''
    :param url: The url of the doujinshi

    :returns: list of urls
    :rtype: list
    '''
    doujinshi = dict()
    doujinshi['url'] = url

    html_doc = download_page(url)
    soup = BeautifulSoup(html_doc, "lxml")
    # find elements by id
    img_table = soup.find("div", {"id": "gdt"})
    try:
        assert img_table != None
    except AssertionError:
        logging.error(
            "img_table is None, maybe encountered warning window", exc_info=True)
        print("print img_table is None, maybe encountered warning window")

    img_div_list = img_table.find_all("div", {"class": "gdtm"})

    eng_name = soup.find("h1", {"id": "gn"}).text
    jap_name = soup.find("h1", {"id": "gj"}).text
    doujinshi["eng_name"] = eng_name
    doujinshi["jap_name"] = jap_name

    # count pages
    number_page = 0

    # img src list
    img_list = []

    page_bar = soup.find("div", {"class": "gtb"})
    number_page = len(page_bar.find_all("td")) - 2

    for page in range(number_page):
        if page == 0:
            _page_url = url
        else:
            _page_url = urljoin(url, "?p="+str(page))

        html_doc = download_page(_page_url)
        soup = BeautifulSoup(html_doc, "lxml")
        # find elements by id
        div_table = soup.find("div", {"id": "gdt"})
        img_div_list = div_table.find_all("div", {"class": "gdtm"})
        for _div in img_div_list:
            sub_img_a = _div.find("a", recursive=True)
            sub_img_url = sub_img_a['href']
            sub_html = download_page(sub_img_url).decode('utf-8')
            sub_soup = BeautifulSoup(sub_html, "lxml")
            img = sub_soup.find("img", {"id": "img"}, recursive=True)
            img_url = img["src"]
            print(img_url)
            img_list.append(img_url)

    doujinshi["img_list"] = img_list

    return doujinshi


def main():
    doujinshi_url = "https://e-hentai.org/g/1178073/30bc24b00a/"

    doujinshi_url = "https://e-hentai.org/g/980918/a3e70a1ca8/"

    _ = doujinshi_parser(doujinshi_url)

    # 如果jap标题为空，就用eng标题
    if _["jap_name"] == "":
        folder = _["eng_name"]
    folder = _["jap_name"]

    from downloader import Downloader
    downloader = Downloader()
    url_queue = _["img_list"]
    print(url_queue)
    downloader.download(url_queue, folder=folder)


if __name__ == "__main__":
    main()
