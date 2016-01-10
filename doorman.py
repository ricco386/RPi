#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.

import RPi.GPIO as GPIO
import time

sensor = 16
door_closed = 0
door_open = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

door_status = door_closed

try:
    while True:
        sensor_status = GPIO.input(sensor)
        if sensor_status != door_status:
            door_status = sensor_status

            if door_status == door_open:
                print('Door is open')
            else:
                print('Door is closed')

        time.sleep(0.1)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup()
