#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import argparse
import RPi.GPIO as GPIO
import time
import logging


class Sensor(object):

    NAME = 'sensor'
    sensor_pin = 0
    sensor_state = 0
    cycle_sleep = 0.1
    thread_exit = False

    def __init__(self, args=[]):
        if args:
            self.args = args

        # Prepare logging configuration
        logconfig = {
            'filename': '/tmp/%s.log' % self.NAME,
            'level': logging.INFO,
            'format': '%(asctime)s %(levelname)-8s %(name)s: %(message)s',
        }

        if hasattr(args, 'log') and args.log:
            logconfig['filename'] = args.log

        if hasattr(args, 'debug') and args.debug:
            logconfig['level'] = logging.DEBUG

        logging.basicConfig(**logconfig)
        logging.info('%s is at your service' % self.NAME)

        if hasattr(args, 'pin') and args.pin:
            self.sensor_pin = args.pin
        elif self.sensor_pin < 0 or self.sensor_pin > 40:
            logging.error('PIN have to between 1 and 40')
            raise Exception

        logging.info('%s PIN: %s' % (self.NAME, self.sensor_pin))
        self.set_gpio()

    def set_gpio(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.sensor_read()

    def pre_sensor_check(self):
        logging.debug('%s pre-read sensor call.', self.NAME)

    def post_sensor_check(self):
        logging.debug('%s post-read sensor call.', self.NAME)

    def sensor_read(self):
        logging.debug('%s sensor reading', self.NAME)

    def sense(self):
        try:
            logging.debug('%s sensing is starting to watch the door status', self.NAME)
            while not self.thread_exit:
                self.pre_sensor_check()
                self.sensor_read()
                self.post_sensor_check()
                time.sleep(self.cycle_sleep)

        except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
            logging.info('You have interupted %s sensing process...', self.NAME)
            GPIO.cleanup()


class Setup(object):

    def args(self, name, desc):
        ap = argparse.ArgumentParser(prog=name, description=desc)
        ap.add_argument('-d', action='store_true', help='Display output.')
        ap.add_argument('-p', type=int, help='Set sensor pin.')
        ap.add_argument('-l', type=str, help='Path where log will be stored.')
        ap.add_argument('--debug', action='store_true', help='Store debug logs.')

        return ap
