#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files, which you should have received as
# part of this distribution.

import RPi.GPIO as GPIO
import time
from logging import INFO, DEBUG
from lookOver.cam import Camera
from lookOver.out import Output


class Sensor():
    cfg = None
    cam = None
    prevState = False
    currState = False
    GPIO_PIR = None
    GPIO_LED = None
    start_time = None

    def __init__(self, config):
        self.out = Output(config)
        self.cfg = config
        self.cam = Camera(config)

        self.GPIO_PIR = None if config.get('global', 'pin_pir') is '' else int(config.get('global', 'pin_pir'))
        self.GPIO_LED = None if config.get('global', 'pin_led') is '' else int(config.get('global', 'pin_led'))
        GPIO.setmode(GPIO.BOARD)
        # Set pin as input
        GPIO.setup(self.GPIO_PIR, GPIO.IN)
        self.out.msg('Setting pin %s for PIR sensor' % self.GPIO_PIR, DEBUG)
        # Set up pin for LED
        if self.GPIO_LED:
            GPIO.setup(self.GPIO_LED, GPIO.OUT)
            self.out.msg('Setting pin %s for LED diode' % self.GPIO_LED, DEBUG)
            self.blink(4)

    def led_enable(self):
        if self.GPIO_LED:
            GPIO.output(self.GPIO_LED, True)
            self.out.msg('Enabling LED diode at pin %s' % self.GPIO_LED, DEBUG)

    def led_disable(self):
        if self.GPIO_LED:
            GPIO.output(self.GPIO_LED, False)
            self.out.msg('Disabling LED diode at pin %s' % self.GPIO_LED, DEBUG)

    def blink(self, number):
        for i in range(0,number):
            self.led_enable()
            time.sleep(0.1)
            self.led_disable()
            time.sleep(0.1)

    def movement(self):
        self.start_time = time.time()
        self.led_enable()
        if self.cam:
            self.cam.start_recording()

    def quiet(self):
        if self.cam:
            self.cam.stop_recording()
        self.led_disable()
        self.out.msg('Detected movement for %s seconds' % (time.time() - self.start_time), DEBUG)

    def settledown(self):
        self.out.msg('Waiting for PIR to settle...', DEBUG)
        # Loop until PIR output is 0
        while GPIO.input(self.GPIO_PIR)==1:
            self.currState = 0
        self.out.msg('... Ready', DEBUG)

    def sense(self):
        try:
            if self.cfg.getboolean('global', 'pin_pir_settle'):
                self.settledown()

            while True:
                time.sleep(0.1)
                self.prevState = self.currState
                self.currState = GPIO.input(self.GPIO_PIR)

                if self.currState != self.prevState:
                    newState = "HIGH" if self.currState else "LOW"
                    self.out.msg("GPIO pin %s is %s" % (self.GPIO_PIR, newState), DEBUG)

                    if self.currState:
                        self.movement()
                    else:
                        self.quiet()

        except KeyboardInterrupt:
            self.out.msg("Keyboard Interrupted...", INFO)
            # Reset GPIO settings
            GPIO.cleanup()
