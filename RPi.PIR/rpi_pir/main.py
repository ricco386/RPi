#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import argparse
from rpi_pir import PIR


def setup_args():
    ap = argparse.ArgumentParser(prog='pir', description='RPi.PIR is using PIR sensor, will permanently sense for HIGH '
                                                         'pin state to detect movement.')
    ap.add_argument('-p', '--pin', type=int, help='GPIO pin number.')
    ap.add_argument('--gpio_bcm', action='store_true', help='Switch PIN to GPIO BCM numbers.')
    ap.add_argument('--failed_notify', type=int, help='Number of failed sensor reading before alerting.')
    ap.add_argument('--cycle_sleep', type=float, help='Sleep time in the loop to slow down sensor readings.')

    return ap.parse_args()


def main():
    pir = PIR(name='PIR')
    args = setup_args()

    if hasattr(args, 'gpio_bcm') and args.gpio_bcm:
        pir.GPIO_BCM = True
        pir.logger.info('Sensor %s mode set to GPIO.BCM (set by script parameter).', pir.NAME)

    if hasattr(args, 'pin') and args.pin:
        pir.PIN = args.pin
        pir.logger.info('Sensor %s at PIN: %s (set by script parameter).', pir.NAME, pir.PIN)

    if hasattr(args, 'failed_notify') and args.failed_notify:
        pir.FAILED_NOTIF = args.failed_notify
        pir.logger.debug('Sensor %s at failed_notify: %s (set by script parameter, overwriting configuration value).',
                         pir.NAME, pir.FAILED_NOTIF)

    if hasattr(args, 'cycle_sleep') and args.cycle_sleep:
        pir.SLEEP = args.cycle_sleep
        pir.logger.debug('Sensor %s at cycle_sleep: %s (set by script parameter).', pir.NAME, pir.SLEEP)

    pir.sense()


if __name__ == "__main__":
    # execute only if run as a script
    main()
