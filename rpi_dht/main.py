#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import sys
import argparse
from dht import Dht
from sensor import Setup


def main():
    args = Setup().args('rpi-dht', 'Python implementation for Adafruit_DHT sensor for Raspberry Pi.')
    args.add_argument('--display', action='store_true', help='Display output.')
    args = args.parse_args()

    sensor = Dht(args)

    if hasattr(args, 'display') and args.display:
        print(sensor.output())
    else:
        sensor.sense()

    sys.exit(0)


if __name__ == "__main__":
    # execute only if run as a script
    main()
