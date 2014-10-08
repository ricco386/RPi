#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files, which you should have received as
# part of this distribution.

import codecs
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from lookOver.__init__ import __version__ as VERSION, __description__ as DESCRIPTION

with codecs.open('README.rst', 'r', encoding='UTF-8') as readme:
    LONG_DESCRIPTION = ''.join(readme)

CLASSIFIERS = [
    'Environment :: Console',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Topic :: Home Automation',
    'Topic :: Security',
    'Topic :: Utilities',
    'Intended Audience :: Other Audience',
    'License :: OSI Approved :: BSD License',
]

packages = [
    'lookOver',
]

setup(
    name = 'lookOver',
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    author = 'Richard Kellner',
    author_email = 'richard.kellner [at] erigones.com',
    url = 'https://github.com/ricco386/lookOver/',
    license = 'New BSD License',
    packages = packages,
    scripts = ['bin/lo'],
    install_requires = ['RPi.GPIO', 'picamera', 'colorama'],
    platforms = 'Linux',
    classifiers = CLASSIFIERS,
    include_package_data = True
)
