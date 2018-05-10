# filename: test_ubuntu.py

import os
from download_benzi import download_benzi

url_first = "https://e-hentai.org/g/1223362/4c9e246925/"
urls = []
urls.append(url_first)
for i in range(1,8+1):
    url_to_append = "https://e-hentai.org/g/1223362/4c9e246925/?p=" + str(i) # 1~8 for 2~9th page
    urls.append(url_to_append)

titleText = "[JOYNET] Menhera-chan" # input by yourself
rootpath = os.environ['HOME'] + "/" +"tmp"
benzi_store_path = rootpath + "/" + titleText

for url in urls:
    download_benzi(sourceUrl=url,benzi_store_path=benzi_store_path)
