#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.

import RPi.GPIO as GPIO
import time
import logging
from doorman.doorman import Doorman

def start():
    d = Doorman()
    d.sense()


if __name__ == '__main__':
    start()
