#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE
# files, which you should have received as part of this distribution.
import setuptools
# noinspection PyPep8Naming
from raspi_mc import __version__ as VERSION

DEPS = ['RPi.Sensor>=0.5.3']

CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'Operating System :: Unix',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Development Status :: 4 - Beta',
    'Topic :: Utilities',
    'Topic :: Home Automation',
    'Topic :: System :: Hardware',
    'Topic :: Terminals'
]

with open("README.rst", "r") as fp:
    sensor_long_description = fp.read()

setuptools.setup(
    name='RPi.MC',
    version=VERSION,
    author="Richard von Kellner",
    author_email="richard.kellner [at] gmail.com",
    url="https://github.com/ricco386/RPi",
    description='Magnetic contact state monitor',
    long_description=sensor_long_description,
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=CLASSIFIERS,
    install_requires=DEPS,
    scripts=['bin/raspi-mc'],
    include_package_data=True
)
