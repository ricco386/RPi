#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import argparse

from raspi_sensor.main import setup_default_mqtt_args
from raspi_pir.pir import PIR


def setup_args():
    ap = argparse.ArgumentParser(prog='raspi-pir',
                                 description='RPi.PIR is using PIR sensor, will permanently sense for HIGH pin state '
                                             'to detect movement. For more info visit: https://github.com/ricco386/RPi')
    setup_default_mqtt_args(ap)
    ap.add_argument('--change_delay', type=int, help='Delay in seconds to report state change.')

    return ap.parse_args()


def main():
    params = setup_args()
    name = 'PIR'
    config = None

    if hasattr(params, 'name') and params.name:
        name = params.name

    if hasattr(params, 'config') and params.config:
        config = params.config

    pir = PIR(name=name, config_path=config)
    pir.setup_args(params)

    if hasattr(params, 'change_delay') and params.change_delay:
        pir.change_delay = params.change_delay

    if hasattr(params, 'status') and params.status:
        pir.sensor_read()
        print('Sensor %s state is %s.', pir.NAME, "HIGH" if pir.sensor_state else "LOW")
    else:
        pir.sense()


if __name__ == "__main__":
    # execute only if run as a script
    main()
