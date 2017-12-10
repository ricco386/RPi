#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import time
from math import floor


class Clock(object):
    time = ''
    exit = False

    def __init__(self):
        self.time = time.asctime()

    def __str__(self):
        return self.time

    def run(self):
        """
        thread function to run the clock on display
        """
        while not self.exit:
            self.time = time.asctime()
            self.sleep()

    def sleep(self):
        """
        Helper function to work out when to wake up for the next round
        """
        start_time = time.time()
        future_time = floor(start_time) + 1
        time.sleep(future_time - start_time)


if __name__ == "__main__":
    print(Clock())
