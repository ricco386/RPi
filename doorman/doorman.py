#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.

import RPi.GPIO as GPIO
import time
import logging


class Doorman():
    sensor_pin = 16
    sensor_state = 0
    door_state = 2 # Set unknown value, due to initial reading
    door_closed = 0
    door_open = 1

    def __init__(self):
        # Prepare logging configuration
        logconfig = {
            'filename': '/tmp/doorman.log',
            'level': logging.INFO,
            'format': '%(asctime)s %(levelname)-8s %(name)s: %(message)s',
        }
        logging.basicConfig(**logconfig)
        logging.info('Doorman is at your service')

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.sensor_read()

    def get_door_state(self):
        if self.door_state == self.door_open:
            return 'Door is open'
        else:
            return 'Door is closed'

    def callback_sensor_read(self):
        logging.info(self.get_door_state())

    def sensor_read(self):
        self.sensor_state = GPIO.input(self.sensor_pin)

        if self.sensor_state != self.door_state:
            logging.debug('Changing sensor state from %s to %s' % (self.door_state, self.sensor_state))
            self.door_state = self.sensor_state
            self.callback_sensor_read()

    def sense(self):
        try:
            logging.debug('Doorman is starting to watch the door status')
            while True:
                self.sensor_read()
                time.sleep(0.1)

        except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
            logging.info('Thank you for using my service, your Doorman!')
            GPIO.cleanup()

