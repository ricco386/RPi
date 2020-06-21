#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE
# files, which you should have received as part of this distribution.
import os
from distutils.core import setup

# noinspection PyPep8Naming
from raspi_pir import __version__ as VERSION

read = lambda fname: open(os.path.join(os.path.dirname(__file__), fname)).read()

DEPS = ['RPi.Sensor',]

CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Development Status :: 4 - Beta',
    'Topic :: Utilities'
]

packages = [
    'raspi_pir',
]

setup(
    name='RPi.PIR',
    version=VERSION,
    description='PIR sensor state monitor',
    long_description=read('README.rst'),
    author='Richard von Kellner',
    author_email='richard.kellner [at] gmail.com',
    url='https://github.com/ricco386/RPi/tree/master/RPi',
    license='MIT',
    packages=packages,
    scripts=['bin/raspi-pir'],
    install_requires=DEPS,
    platforms='any',
    classifiers=CLASSIFIERS,
    include_package_data=True
)
