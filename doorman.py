#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.

import RPi.GPIO as GPIO
import time

class Doorman():
    sensor_pin = 16
    sensor_state = 0
    door_state = 2 # Set unknown value, due to initial reading
    door_closed = 0
    door_open = 1

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.sensor_read()

    def print_door_state(self):
        if self.door_state == self.door_open:
            print('Door is open')
        else:
            print('Door is closed')

    def sensor_read(self):
        self.sensor_state = GPIO.input(self.sensor_pin)

        if self.sensor_state != self.door_state:
            self.door_state = self.sensor_state
            self.print_door_state()

    def sense(self):
        try:
            while True:
                self.sensor_read()
                time.sleep(0.1)

        except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
            GPIO.cleanup()

d = Doorman()
d.sense()
