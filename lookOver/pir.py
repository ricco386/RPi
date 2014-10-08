#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files, which you should have received as
# part of this distribution.

import RPi.GPIO as GPIO
import time
from logging import DEBUG
from lookOver.cam import Camera
from lookOver.out import Output


class Sensor():
    args = None
    prevState = False
    currState = False
    GPIO_PIR = None
    GPIO_LED = None

    def __init__(self, args):
        self.out = Output(args)
        self.args = args
        self.GPIO_PIR = 7
        if self.args.pir is not None:
            self.GPIO_PIR = self.args.pir

        self.GPIO_LED = 17
        if self.args.led is not None:
            self.GPIO_LED = self.args.led

        GPIO.setmode(GPIO.BOARD)
        # Set pin as input
        GPIO.setup(self.GPIO_PIR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.out.msg('Setting pin %s for PIR sensor' % self.GPIO_PIR, DEBUG)
        # Set up pin for LED
        # GPIO.setup(self.GPIO_LED, GPIO.OUT)
        # self.out.msg('Setting pin for LED diode %s' % self.GPIO_LED, DEBUG)

    def sense(self):
        cam = Camera(self.args)

        while True:
            time.sleep(0.1)
            self.prevState = self.currState
            self.currState = GPIO.input(self.GPIO_PIR)

            if self.currState != self.prevState:
                newState = "HIGH" if self.currState else "LOW"
                self.out.msg("GPIO pin %s is %s" % (self.GPIO_PIR, newState), DEBUG)

                if self.currState:
                    cam.start_recording()
                else:
                    cam.stop_recording()
