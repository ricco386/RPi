#!/usr/bin/python
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
        if args.loglevel:
            self.logger.setLevel(args.loglevel)
            self.default_lvl = args.loglevel
        else:
            self.logger.setLevel(logging.DEBUG)
            self.default_lvl = logging.DEBUG

    def log(self, msg, level):
        self.logger.log(level, msg)

    def prnt(self, msg, color=None, back=None, stl=None):
        clr = ''
        if stdout.isatty():
            # We are printing on screen with some color
            if color:
                clr += getattr(Fore, color)
            if back:
                clr += getattr(Back, back)
            if stl:
                clr += getattr(Style, stl)
        print clr + msg
        if stdout.isatty() and (color or back or stl):
            # Recet colors on terminal to default state
            print Fore.RESET + Back.RESET + Style.RESET_ALL

    def msg(self, msg, level=None, color=None, back=None, stl=None):
        if level is None:
            level = self.default_lvl
        self.log(msg, level)

        if color is None:
            if level == logging.CRITICAL:
                color = 'RED'
                stl = 'BRIGHT'
            if level == logging.ERROR:
                color = 'RED'
            if level == logging.WARNING:
                color = 'YELLOW'
            if level == logging.INFO:
                color = 'GREEN'
                stl = 'BRIGHT'
            else:
                stl = 'DIM'
        self.prnt(msg, color=color, back=back, stl=stl)
