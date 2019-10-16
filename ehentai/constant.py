# coding: utf-8
from __future__ import unicode_literals, print_function
import os

BASE_URL = os.getenv('EHENTAI', 'https://e-hentai.org/')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}

PROXY = {}
