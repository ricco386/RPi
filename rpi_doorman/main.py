#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.

import argparse
from doorman import Doorman


def setup_args():
    ap = argparse.ArgumentParser(prog='doorman',
            description='RPi.Doorman is using adafruit magnetic contact switch (door sensor), will permanently sense for door status and its changes.'
            )
    ap.add_argument('-c', action='store_true', help='Current door status will be shown.')
    ap.add_argument('-p', type=int, help='Pin number, for GPIO magnetic contact switch (door sensor).')
    ap.add_argument('-l', type=str, help='Log path, where logs will be stored.')
    ap.add_argument('-d', action='store_true', help='Debug mode, wheather store debug info in log.')

    return ap.parse_args()


def main():
    args = setup_args()
    d = Doorman(args)

    if hasattr(args, 'c') and args.c:
        print(d.get_door_state())
    else:
        d.sense()


if __name__ == "__main__":
    # execute only if run as a script
    main()
