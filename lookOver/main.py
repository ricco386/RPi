#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files, which you should have received as
# part of this distribution.

import argparse
import textwrap
from lookOver import __version__ as VERSION, __description__ as DESCRIPTION
from lookOver import pir

def setup_args():
    ap = argparse.ArgumentParser(prog='lookOver',
            description='%(prog)s - ' + DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''\
                useful links:
                 - Wiki: https://github.com/ricco386/lookOver/wiki
                 - Bug Tracker: https://github.com/ricco386/lookOver/issues
                 - Twitter: https://twitter.com/ricco386

                author:
                  written by Richard Kellner (richard.kellner (at) erigones.com)

                license:
                  This software is licensed as described in the README.rst and LICENSE files,
                  which you should have received as part of this distribution.
                '''))
    # Sensors
    ap.add_argument('-p', '--pir', type=int, help='Set pin number on which is PIR sensor connected')
    ap.add_argument('--settle', action='store_true', help='Wait for PIR sensor to settle, before start')
    ap.add_argument('-l', '--led', type=int, help='Set pin number on which LED will be enabled when motion sensed')
    # Camera
    ap.add_argument('--width', type=int, help='Set camera resolution...')
    ap.add_argument('--height', type=int, help='Set camera resolution...')
    ap.add_argument('--nopicture', action='store_true', help='Disable picture at movement trigger')
    ap.add_argument('--novideo', action='store_true', help='Disable video recording at movement trigger')
    ap.add_argument('--hflip', action='store_true',
                    help='Retrieves of sets whether the renderer\'s output is horizontally flipped')
    ap.add_argument('--vflip', action='store_true',
                    help='Retrieves of sets whether the renderer\'s output is vertically flipped')
    ap.add_argument('--framerate', '-f', help='Set camera framerate...', nargs='?', default=False)
    # App
    ap.add_argument('-v', '--verbosity', type=int, choices=[10, 20, 30, 40, 50],
            help="Set output verbosity (50: CRITICAL, 40: ERROR, 30: WARNING, 20: INFO, 10: DEBUG)")
    ap.add_argument('--version', action='version', version=('%(prog)s '+ VERSION))
    return ap.parse_args()

def start():
    lo = pir.Sensor(setup_args())
    lo.sense()

if __name__ == '__main__':
    start()
