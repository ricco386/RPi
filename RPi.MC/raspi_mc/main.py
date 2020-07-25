#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import argparse

from raspi_sensor.main import setup_default_mqtt_args
from raspi_mc.magnetic_contact import MC


def setup_args():
    ap = argparse.ArgumentParser(prog='raspi-mc',
                                 description='RPi.MC is using magnetic contact switch (door sensor), will permanently '
                                             'sense for HIGH pin state to detect door status. For more info visit: '
                                             'https://github.com/ricco386/RPi')
    setup_default_mqtt_args(ap)

    return ap.parse_args()


def main():
    params = setup_args()
    name = 'Magnetic_Contact'
    config = None

    if hasattr(params, 'name') and params.name:
        name = params.name

    if hasattr(params, 'config') and params.config:
        config = params.config

    mc = MC(name=name, config_path=config)
    mc.setup_args(params)

    if hasattr(params, 'status') and params.status:
        mc.sensor_read()
        print(mc.get_door_state())
    else:
        mc.sense()


if __name__ == "__main__":
    # execute only if run as a script
    main()
