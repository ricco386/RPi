#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import argparse
import RPi.GPIO as GPIO
import time
import logging
import requests


class Sensor(object):

    NAME = 'sensor'
    sensor_pin = 0
    sensor_state = 0
    cycle_sleep = 0.1
    thread_exit = False

    log = None

    url = False
    token = False
    username = False
    password = False

    def __init__(self, args=[]):
        if args:
            self.args = args

        # Prepare logging configuration
        self.set_logging()
        self.log.info('%s is at your service...' % self.NAME)

        if hasattr(args, 'server') and args.server:
            self.url = args.server
            self.log.info('Notify server: %s' % self.url)

        if hasattr(args, 'token') and args.token:
            self.token = args.token
            self.log.info('Authenticate on server via token.')

        if hasattr(args, 'username') and args.username and hasattr(args, 'password') and args.password:
            self.username = args.username
            self.password = args.password
            self.log.info('Authenticate on server via username and password.')

        if hasattr(args, 'pin') and args.pin:
            self.sensor_pin = args.pin
        elif self.sensor_pin < 0 or self.sensor_pin > 40:
            self.log.error('PIN have to between 1 and 40')
            raise Exception

        self.log.info('Sensor at PIN: %s' % self.sensor_pin)
        self.set_gpio()

    def set_logging(self):
        logconfig = {
            'filename': '/tmp/%s.log' % self.NAME,
            'level': logging.INFO,
            'format': '%(asctime)s %(levelname)-8s %(name)s: %(message)s',
        }

        if hasattr(self.args, 'log') and self.args.log:
            logconfig['filename'] = self.args.log

        if hasattr(self.args, 'debug') and self.args.debug:
            logconfig['level'] = logging.DEBUG

        logging.basicConfig(**logconfig)
        self.log = logging.getLogger(self.NAME)

    def set_gpio(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.sensor_read()

    def pre_sensor_read_callback(self):
        self.log.debug('Pre-read sensor callback.')

    def post_sensor_read_callback(self):
        self.log.debug('Post-read sensor callback.')

    def sensor_read_callback(self):
        self.log.debug('Sensor read callback')

    def sensor_read(self):
        self.pre_sensor_read_callback()
        self.sensor_read_callback()
        self.post_sensor_read_callback()

    def sense(self):
        try:
            self.log.debug('Starting permanent sensing process...')

            while not self.thread_exit:
                self.sensor_read()
                time.sleep(self.cycle_sleep)

                if self.thread_exit:
                    self.log.info('Signal send to interupted sensing process...')

        except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
            self.log.info('You have interupted sensing process...')

        GPIO.cleanup()

    def post_data(self, postdata):
        if not self.url:
            self.log.error('Trying to post data, but no server bas been defined!')
            raise ValueError('Server has not been defined!')

        if self.token:
            headers = {
                'Authorization': 'Token '+ self.token
            }
            r = requests.post(self.url, headers=headers, data=postdata)
        elif self.username and self.password:
            r = requests.post(self.url, auth=(self.username, self.password), data=postdata)
        else:
            r = requests.post(self.url, data=postdata)

        if r.status_code == requests.codes.ok:
            self.log.info("HTTP Post to %s was successful", self.url)
            return True
        else:
            self.log.error("HTTP Post to %s has failed...", self.url)
            return False


class Setup(object):

    def args(self, name, desc):
        ap = argparse.ArgumentParser(prog=name, description=desc)
        ap.add_argument('-d', action='store_true', help='Display output.')
        ap.add_argument('-p', '--pin', type=int, help='Set sensor pin.')
        ap.add_argument('-l', '--log', type=str, help='Path where log will be stored.')
        ap.add_argument('-s', '--server', type=str, help='Server where data will be posted.')
        ap.add_argument('-t', '--token', type=str, help='Security token for server authentication.')
        ap.add_argument('--username', type=str, help='Username for server authentication.')
        ap.add_argument('--password', type=str, help='Password for server authentication.')
        ap.add_argument('--debug', action='store_true', help='Store debug logs.')

        return ap
