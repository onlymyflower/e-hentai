#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: onlymyflower
# Date: 2019.5.2
from __future__ import unicode_literals, print_function
import signal
import platform

from ehentai.cmdline import banner, cmd_parser
from ehentai.logger import logger
from ehentai.constant import HEADERS, BASE_URL
from ehentai.comic import Comic
from ehentai.downloader import Downloader
from ehentai.utils import generate_html
from ehentai.parser import doujinshi_parser


def main():
    banner()

    logger.info('ehentai: {0}'.format(BASE_URL))
    options = cmd_parser()

    doujinshi_urls = []

    if not doujinshi_urls:
        doujinshi_urls = options.url

    if doujinshi_urls:
        for doujinshi_url in doujinshi_urls:
            logger.info('Starting to download doujinshi: %s' % doujinshi_url)
            headers = HEADERS
            _ = doujinshi_parser(doujinshi_url)
            # 如果jap标题为空，就用eng标题
            folder = _["jap_name"]
            if _["jap_name"] == "":
                folder = _["eng_name"]
            downloader = Downloader(thread=options.threads,
                                    timeout=options.timeout)
            url_queue = _["img_list"]
            downloader.download(url_queue, headers=headers, folder=folder)


def signal_handler(signal, frame):
    logger.error('Ctrl-C signal received. Stopping...')
    exit(1)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    main()
