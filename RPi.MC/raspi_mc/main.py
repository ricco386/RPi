#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import argparse
from .magnetic_contact import MC


def setup_args():
    ap = argparse.ArgumentParser(prog='raspi-mc', description='RPi.MC is using adafruit magnetic contact switch (door '
                                                              'sensor), will permanently sense for door status and its '
                                                              'changes.')
    ap.add_argument('-s', '--status', action='store_true', help='Current door status will be shown.')
    ap.add_argument('-p', '--pin', type=int, help='Pin number, for GPIO magnetic contact switch (door sensor).')
    ap.add_argument('--name', type=str, help='Set sensor name for logging.')
    ap.add_argument('--gpio_bcm', action='store_true', help='Switch PIN to GPIO BCM numbers.')
    ap.add_argument('--failed_notify', type=int, help='Number of failed sensor reading before alerting.')
    ap.add_argument('--cycle_sleep', type=float, help='Sleep time in the loop to slow down sensor readings.')

    return ap.parse_args()


def main():
    params = setup_args()
    name = 'Magnetic Contact'

    if hasattr(params, 'name') and params.name:
        name = params.name

    d = MC(name=name, params=params)

    if hasattr(params, 'status') and params.status:
        d.sensor_read()
        print(d.get_door_state())
    else:
        d.sense()


if __name__ == "__main__":
    # execute only if run as a script
    main()
