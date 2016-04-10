#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import sys
import argparse
from dht import Dht, DhtSetup


def main():
    args = DhtSetup().args('rpi-dht', 'Python implementation for Adafruit_DHT sensor for Raspberry Pi.').parse_args()
    sensor = Dht(args)

    if hasattr(args, 'd') and args.d:
        print(sensor.output())
    else:
        sensor.sense()

    sys.exit(0)


if __name__ == "__main__":
    # execute only if run as a script
    main()
