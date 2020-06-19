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
    ap.add_argument('--name', type=str, help='Set sensor name for logging.')
    ap.add_argument('--gpio_bcm', action='store_true', help='Switch PIN to GPIO BCM numbers.')
    ap.add_argument('--failed_notify', type=int, help='Number of failed sensor reading before alerting.')
    ap.add_argument('--cycle_sleep', type=float, help='Sleep time in the loop to slow down sensor readings.')
    ap.add_argument('--mqtt_topic', type=str, help='Set topic for MQTT where sensor will publish data.')
    ap.add_argument('--temperature', action='store_true', help='Display temperature in *C.')
    ap.add_argument('--humidity', action='store_true', help='Display humidity in percent.')

    return ap.parse_args()


def main():
    params = setup_args()
    name = 'DHT'

    if hasattr(params, 'name') and params.name:
        name = params.name

    d = Dht(name=name, params=params)

    if hasattr(params, 'status') and params.status:
        d.sensor_read()
        print(d.output())
    elif hasattr(params, 'temperature') and params.temperature:
        d.sensor_read()
        print(d.output(temp=True, desc=False))
    elif hasattr(params, 'humidity') and params.humidity:
        d.sensor_read()
        print(d.output(hum=True, desc=False))
    else:
        d.sense()


if __name__ == "__main__":
    # execute only if run as a script
    main()
