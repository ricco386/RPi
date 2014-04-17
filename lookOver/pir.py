#!/usr/bin/python
#
# Detect movement using a PIR module

import RPi.GPIO as GPIO
import time

class Sensor():

    current_motion = 0
    previous_motion = 0

    def __init__(self, pin_):
        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)

        if pin_ is None:
            GPIO_PIR = pin_
        else:
            GPIO_PIR = 17

        print "PIR Module Test (CTRL-C to exit)"

        # Set pin as input
        GPIO.setup(GPIO_PIR,GPIO.IN)

        while GPIO.input(GPIO_PIR)==1:
            self.current_motion = 0

    def sence():
        print "Initiating PIR module"

        try:

            # Loop until users quits with CTRL-C
            while True:

                # Read PIR state
                self.current_motion = GPIO.input(GPIO_PIR)

                if self.current_motion==1 and self.previous_motion==0:
                    # PIR is triggered
                    print "  Motion detected!"
                    # Record previous state
                    self.previous_motion=1
                elif self.current_motion==0 and self.previous_motion==1:
                    # PIR has returned to ready state
                    print "  Waiting for Motion"
                    self.previous_motion=0

                # Wait for 10 milliseconds
                time.sleep(0.01)

        except KeyboardInterrupt:
            print "Quit"
            # Reset GPIO settings

        GPIO.cleanup()
