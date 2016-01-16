#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.

import RPi.GPIO as GPIO
import time
import logging


class Doorman():
    args = []
    sensor_pin = 16
    sensor_state = 0
    door_state = 2 # Set unknown value, due to initial reading
    door_closed = 0
    door_open = 1

    def __init__(self, args=[]):
        if args:
            self.args = args

        # Prepare logging configuration
        logconfig = {
            'filename': '/tmp/doorman.log',
            'level': logging.INFO,
            'format': '%(asctime)s %(levelname)-8s %(name)s: %(message)s',
        }

        if hasattr(args, 'log') and args.log:
            logconfig['filename'] = args.log

        if hasattr(args, 'debug') and args.debug:
            logconfig['level'] = logging.DEBUG

        logging.basicConfig(**logconfig)
        logging.info('Doorman is at your service')

        if hasattr(args, 'pin') and args.pin:
            self.sensor_pin = args.pin
        logging.debug('Sensor PIN: %s', self.sensor_pin)

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.sensor_read()

    def get_door_state(self):
        if self.door_state == self.door_open:
            return 'Door is open'
        else:
            return 'Door is closed'

    def notify(self):
        if hasattr(self.args, 'notify') and self.args.notify:
            try:
                import requests
            except ImportError:
                logger.error('Can not import requests library. Make sure it is installed!')
            else:
                r = requests.post("http://127.0.0.1:8922/doorman_update",
                        data = {
                            "user": self.args.notify,
                            "msg": self.get_door_state()
                            }
                        )
                log = 'Notification response code: %s (user: %s, msg: %s)' % (r.status_code, self.args.notify,
                        self.get_door_state())

                if r.status_code != requests.codes.ok:
                    logging.error(log)
                else:
                    logging.debug(log)

    def callback_sensor_read(self):
        logging.info(self.get_door_state())

    def sensor_read(self):
        self.sensor_state = GPIO.input(self.sensor_pin)

        if self.sensor_state != self.door_state:
            logging.debug('Changing sensor state from %s to %s' % (self.door_state, self.sensor_state))
            self.door_state = self.sensor_state
            self.callback_sensor_read()
            self.notify()

    def sense(self):
        try:
            logging.debug('Doorman is starting to watch the door status')
            while True:
                self.sensor_read()
                time.sleep(0.1)

        except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
            logging.info('Thank you for using my service, your Doorman!')
            GPIO.cleanup()

