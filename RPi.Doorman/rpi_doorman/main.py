#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.

import argparse
from rpi_doorman import Doorman


def setup_args():
    ap = argparse.ArgumentParser(prog='doorman',
            description='RPi.Doorman is using adafruit magnetic contact switch (door sensor), will permanently sense for door status and its changes.'
            )
    ap.add_argument('-s', '--status', action='store_true', help='Current door status will be shown.')
    ap.add_argument('-p', '--pin', type=int, help='Pin number, for GPIO magnetic contact switch (door sensor).')
    ap.add_argument('--failed_notify', type=int, help='Number of failed sensor reading before alerting.')
    ap.add_argument('--cycle_sleep', type=int, help='Number of failed sensor reading before alerting.')

    return ap.parse_args()


def main():
    d = Doorman()
    args = setup_args()

    if hasattr(args, 'pin') and args.pin:
        d.PIN = args.pin
        d.logger.info('Sensor %s at PIN: %s (set by script parameter, overwriting configuration value).', d.NAME, d.PIN)

    if hasattr(args, 'failed_notify') and args.failed_notify:
        d.FAILED_NOTIF = args.failed_notify
        d.logger.debug('Sensor %s at failed_notify: %s (set by script parameter, overwriting configuration value).',
                       d.NAME, d.FAILED_NOTIF)

    if hasattr(args, 'cycle_sleep') and args.cycle_sleep:
        d.SLEEP = args.cycle_sleep
        d.logger.debug('Sensor %s at cycle_sleep: %s (set by script parameter, overwriting configuration value).',
                       d.NAME, d.SLEEP)

    if hasattr(args, 'status') and args.status:
        d.sensor_read()
        print(d.get_door_state())
    else:
        d.sense()


if __name__ == "__main__":
    # execute only if run as a script
    main()
