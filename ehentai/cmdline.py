# coding: utf-8
from __future__ import print_function
import sys
from optparse import OptionParser
from ehentai import __version__
try:
    from itertools import ifilter as filter
except ImportError:
    pass

import ehentai.constant as constant
from ehentai.utils import urlparse, generate_html
from ehentai.logger import logger

try:
    if sys.version_info < (3, 0, 0):
        import codecs
        import locale
        sys.stdout = codecs.getwriter(
            locale.getpreferredencoding())(sys.stdout)
        sys.stderr = codecs.getwriter(
            locale.getpreferredencoding())(sys.stderr)

except NameError:
    # python3
    pass


def banner():
    logger.info(u'''ehentai ver %s: E-Hentai.org
/***
e-hentai
 */
 你是变态嘛？''' % __version__)


def cmd_parser():
    parser = OptionParser()
    parser.add_option("--url", "-u", type='string', dest='url',
                      action='store', help='doujinshi url set, e.g. https://e-hentai.org/g/1178073/30bc24b00a/')
    parser.add_option('--threads', '-t', type='int', dest='threads', action='store', default=4,
                      help='thread count for downloading comic')
    parser.add_option('--timeout', '-T', type='int', dest='timeout', action='store', default=30,
                      help='timeout for downloading comic')
    try:
        sys.argv = list(map(lambda x: unicode(
            x.decode(sys.stdin.encoding)), sys.argv))
    except (NameError, TypeError):
        pass
    except UnicodeDecodeError:
        exit(0)

    args, _ = parser.parse_args(sys.argv[1:])

    if args.url:
        _ = map(lambda id: id.strip(), args.url.split(','))
        args.url = set(_)

    return args
