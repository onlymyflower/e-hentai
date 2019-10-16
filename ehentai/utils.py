#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Sep-30-19 16:57
# @Author  : onlymyflower
# @Link    : http://example.org

from __future__ import unicode_literals, print_function
import sys
import os
import string
import requests


def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data


class _Singleton(type):
    """ A metaclass that creates a Singleton base class when called. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                _Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(_Singleton(str('SingletonMeta'), (object,), {})):
    pass


def urlparse(url):
    try:
        from urlparse import urlparse
    except ImportError:
        from urllib.parse import urlparse

    return urlparse(url)


def readfile(path):
    loc = os.path.dirname(__file__)

    with open(os.path.join(loc, path), 'r') as file:
        return file.read()


def find_between(s, first, last, begin=0):
    try:
        start = s.index(first, begin) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ''


def generate_html(output_dir='.', doujinshi_obj=None):
    image_html = ''

    if doujinshi_obj is not None:
        doujinshi_dir = os.path.join(output_dir, doujinshi_obj.filename)
    else:
        doujinshi_dir = '.'

    file_list = os.listdir(doujinshi_dir)
    file_list.sort()

    for image in file_list:
        if not os.path.splitext(image)[1] in ('.jpg', '.png'):
            continue

        image_html += '<img src="{0}" class="image-item"/>\n'\
            .format(image)

    html = readfile('viewer/index.html')
    css = readfile('viewer/styles.css')
    js = readfile('viewer/scripts.js')

    if doujinshi_obj is not None:
        title = doujinshi_obj.name
        if sys.version_info < (3, 0):
            title = title.encode('utf-8')
    else:
        title = 'nHentai HTML Viewer'

    data = html.format(TITLE=title, IMAGES=image_html, SCRIPTS=js, STYLES=css)
    try:
        if sys.version_info < (3, 0):
            with open(os.path.join(doujinshi_dir, 'index.html'), 'w') as f:
                f.write(data)
        else:
            with open(os.path.join(doujinshi_dir, 'index.html'), 'wb') as f:
                f.write(data.encode('utf-8'))

        logger.log(15, 'HTML Viewer has been write to \'{0}\''.format(
            os.path.join(doujinshi_dir, 'index.html')))
    except Exception as e:
        logger.warning('Writen HTML Viewer failed ({})'.format(str(e)))


def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
Uses a whitelist approach: any characters not present in valid_chars are
removed. Also spaces are replaced with underscores.

Note: this method may produce invalid filenames such as ``, `.` or `..`
When I use this method I prepend a date string like '2009_01_15_19_46_32_'
and append a file extension like '.txt', so I avoid the potential of using
an invalid filename.

"""
    valid_chars = "-_.()[] %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
    if len(filename) > 100:
        filename = filename[:100] + '...]'

    # Remove [] from filename
    filename = filename.replace('[]', '')
    return filename
