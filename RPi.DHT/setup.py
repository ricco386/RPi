#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE
# files, which you should have received as part of this distribution.
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# noinspection PyPep8Naming
from raspi_dht import __version__ as VERSION

read = lambda fname: open(os.path.join(os.path.dirname(__file__), fname)).read()

DEPS = ['Adafruit_Python_DHT', 'RPi.Sensor',]

CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Development Status :: 3 - Alpha',
    'Topic :: Utilities'
]

packages = [
    'raspi_dht',
]

setup(
    name='RPi.DHT',
    version=VERSION,
    description='Python implementation for Adafruit_DHT sensor for Raspberry Pi.',
    long_description=read('README.rst'),
    author='Richard Kellner',
    author_email='richard.kellner [at] gmail.com',
    url='https://github.com/ricco386/RPi',
    license='MIT',
    packages=packages,
    scripts=['bin/raspi-dht'],
    install_requires=DEPS,
    platforms='any',
    classifiers=CLASSIFIERS,
    include_package_data=True
)
