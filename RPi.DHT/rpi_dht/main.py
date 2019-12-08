#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import argparse
from dht import Dht


def setup_args():
    ap = argparse.ArgumentParser(prog='rpi-dht', description='''Python implementation for Adafruit_DHT sensor for
    Raspberry Pi. Script loads configuration from sensor.cfg that has to be created and run in infinte loop. For more
    info visit: https://github.com/ricco386/RPi.DHT''')
    ap.add_argument('-s', '--status', action='store_true', help='Current DHT sensor status will be shown.')
    ap.add_argument('-p', '--pin', type=int, help='Pin number, for GPIO magnetic contact switch (door sensor).')
    ap.add_argument('--gpio_bcm', action='store_true', help='Switch PIN to GPIO BCM numbers.')
    ap.add_argument('--failed_notify', type=int, help='Number of failed sensor reading before alerting.')
    ap.add_argument('--cycle_sleep', type=int, help='Number of failed sensor reading before alerting.')
    ap.add_argument('--temperature', action='store_true', help='Display temperature in *C.')
    ap.add_argument('--humidity', action='store_true', help='Display humidity in percent.')

    return ap.parse_args()


def main():
    d = Dht()
    args = setup_args()

    if hasattr(args, 'gpio_bcm') and args.gpio_bcm:
        d.GPIO_BCM = True
        d.logger.info('Sensor %s mode set to GPIO.BCM (set by script parameter, overwriting configuration value).',
                      d.NAME)

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
        print(d.output())
    elif hasattr(args, 'temperature') and args.temperature:
        d.sensor_read()
        print(d.output(temp=True, desc=False))
    elif hasattr(args, 'humidity') and args.humidity:
        d.sensor_read()
        print(d.output(hum=True, desc=False))
    else:
        d.sense()


if __name__ == "__main__":
    # execute only if run as a script
    main()
