#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import argparse
from .pir import PIR


def setup_args():
    ap = argparse.ArgumentParser(prog='raspi-pir', description='RPi.PIR is using PIR sensor, will permanently sense '
                                                               'for HIGH pin state to detect movement.')
    ap.add_argument('-p', '--pin', type=int, help='GPIO pin number.')
    ap.add_argument('--name', type=str, help='Set sensor name for logging.')
    ap.add_argument('--gpio_bcm', action='store_true', help='Switch PIN to GPIO BCM numbers.')
    ap.add_argument('--failed_notify', type=int, help='Number of failed sensor reading before alerting.')
    ap.add_argument('--cycle_sleep', type=float, help='Sleep time in the loop to slow down sensor readings.')
    ap.add_argument('--mqtt_topic', type=str, help='Set topic for MQTT where sensor will publish data.')
    ap.add_argument('--change_delay', type=int, help='Delay in seconds to report state change.')

    return ap.parse_args()


def main():
    params = setup_args()
    name = 'PIR'

    if hasattr(params, 'name') and params.name:
        name = params.name

    pir = PIR(name=name, params=params)

    if hasattr(params, 'change_delay') and params.change_delay:
        pir.change_delay = params.change_delay

    pir.sense()


if __name__ == "__main__":
    # execute only if run as a script
    main()
