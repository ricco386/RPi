#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import argparse

from raspi_sensor.main import setup_default_mqtt_args
from raspi_relay.relay import Relay


def setup_args():
    ap = argparse.ArgumentParser(prog='raspi-relay',
                                 description='RPi.Relay can change relay state, via Raspberry Pi GPIO.',
                                 epilog='For more info visit: https://github.com/ricco386/RPi/tree/master/RPi.Relay')
    setup_default_mqtt_args(ap)

    return ap.parse_args()


def main():
    params = setup_args()
    name = 'Relay'

    if hasattr(params, 'name') and params.name:
        name = params.name

    r = Relay(name=name)
    r.setup_args(params)

    if hasattr(params, 'status') and params.status:
        r.sensor_read()
        print(r.get_relay_state())
    else:
        r.sense()


if __name__ == "__main__":
    # execute only if run as a script
    main()
