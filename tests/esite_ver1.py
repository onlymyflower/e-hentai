# encoding=utf-8
# Author: onlymyflower
# Date: 2018.4.25
import requests
from bs4 import BeautifulSoup
import urllib
import requests

DEF_DEBUG = 0

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

test_filename = 'test.html'

def main():
    url = 'https://e-hentai.org/g/1187477/edec63445c/'
    html_doc = download_page(url).decode('utf-8')
    soup = BeautifulSoup(html_doc,"lxml")
    with open(test_filename, 'w') as f:
        print(html_doc, file=f)

    # find elements by id
    img_table = soup.find("div", {"id": 'gdt'})
#     print(img_table)
    imgs_list = img_table.find_all("div", {"class": 'gdtm'})
#     print(imgs_list)
    tmp = imgs_list[0].find("a", recursive=True)
    print(tmp['href']) # got the sub link, like: https://e-hentai.org/s/a04c2bf142/1187477-1
    sub_url = tmp['href']
#     print(sub_url)
    sub_html = download_page(sub_url).decode('utf-8') # ....复制粘贴不够仔细
    sub_soup = BeautifulSoup(sub_html,"lxml")
#     sub_filename = "rqb.html" # emmmmm，原来打开的不是那个。。。
#     with open(sub_filename, 'w') as f:
#         print(sub_html, file=f)
#     print(sub_soup)
    # got the sub page
    rbq = sub_soup.find_all("div", {"id": "i3"}, recursive=True) # id="i3", the frontend enginer should be fired
    # <img id="img">
    # try it back again
    img = sub_soup.find("img", {"id": "img"}, recursive=True)
    img_url = img["src"]


    # 10年的代码了，估计接口早换了。。。    testfile = urllib.URLopener()
#     testfile.retrieve(img_url, "iloverbs.jpg")
    img_get = requests.get(img_url)
    image_name = "test.jpg"
    with open(image_name, "wb") as f:
        f.write(img_get.content)

    # 好了，整理一下代码
    # module 'urllib' has no attribute 'urlretrieve'
    # output:
    # hao le
    # 但是url是带参数的，怎么获取文件。。。，加&
    # en, 不加也可以

    # great, img is a open label, maybe cannot be found, try a outside
#     rbq.find_all()
#     print(imgs)
#     for sub_img in imgs_list:
        # TODO
#         print("sb")

if __name__ == '__main__':
    main()
