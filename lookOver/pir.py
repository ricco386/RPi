#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import picamera
import datetime
import logging
import os
import logging
import subprocess
from argparse import ArgumentParser
from lookOver.cam import Camera

class Sensor():
    args = None
    prevState = False
    currState = False
    GPIO_PIR = None
    GPIO_LED = None

    def __init__(self, args):
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
        #logging.info('Setting pin for PIR sensor %s' % self.GPIO_PIR)
        # Set up pin for LED
        # GPIO.setup(self.GPIO_LED, GPIO.OUT)
        # logging.info('Setting pin for LED diode %s' % self.GPIO_LED)

    def sense(self):
        cam = Camera(self.args)

        while True:
            time.sleep(0.1)
            self.prevState = self.currState
            self.currState = GPIO.input(self.GPIO_PIR)

            if self.currState != self.prevState:
                newState = "HIGH" if self.currState else "LOW"
                #logging.debug("GPIO pin %s is %s" % (self.GPIO_PIR, newState))

                if self.currState:
                    cam.start_recording()
                else:
                    cam.stop_recording()
