#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files, which you should have received as
# part of this distribution.

import datetime
import logging
from sys import stdout
from colorama import Fore, Back, Style


class Output():
    default_lvl = None
    logger = None

    def __init__(self, args):
        today = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        #logging.basicConfig(format='%(asctime)s :%(levelname)s: %(message)s',filename=today+'.log',level=logging.INFO)

        self.logger = logging.getLogger(__name__)
        print args.verbosity
        if args.verbosity:
            self.logger.setLevel(args.verbosity)
            self.default_lvl = args.verbosity
        else:
            self.logger.setLevel(logging.INFO)
            self.default_lvl = logging.INFO
        print self.default_lvl

    def log(self, msg, level):
        self.logger.log(level, msg)

    def prnt(self, msg, level):
        if stdout.isatty():
            # We are printing on screen with some color
            if level == logging.CRITICAL:
                msg = Fore.RED + Style.BRIGHT + msg
            elif level == logging.ERROR:
                msg = Fore.RED + msg
            elif level == logging.WARNING:
                msg = Fore.YELLOW + msg
            elif level == logging.INFO:
                msg = Fore.GREEN + Style.BRIGHT + msg
            elif level == logging.DEBUG:
                msg = Fore.MAGENTA + msg
            print msg + Fore.RESET + Back.RESET + Style.RESET_ALL
        else:
            # Recet colors on terminal to default state
            print msg

    def msg(self, msg, level=None):
        if level is None:
            level = self.default_lvl
        if level >= self.default_lvl:
            self.prnt(msg, level)
        self.log(msg, level)
