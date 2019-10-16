#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import sys
import codecs
from setuptools import setup, find_packages
from ehentai import __version__, __author__, __email__

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]


def long_description():
    with codecs.open('README.rst', 'rb') as readme:
        if not sys.version_info < (3, 0, 0):
            return readme.read().decode('utf-8')


setup(
    name='ehentai',
    version=__version__,
    author=__author__,
    author_email=__email__,
    description='e-hentai.com comics downloader',
    long_description=long_description(),
    keywords=['ehentai', 'e-hentai', 'comics'],
    maintainer=__author__,
    maintainer_email=__email__,
    license='MIT',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/onlymyflower/e-hentai',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': [
            'ehentai=ehentai.command:main',
        ]
    },
)
