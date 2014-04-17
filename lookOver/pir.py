#!/usr/bin/python
#
# Detect movement using a PIR module

import RPi.GPIO as GPIO
import time
import picamera

class Sensor():

    current_motion = 0
    previous_motion = 0
    GPIO_PIR = None
    GPIO_LED = None

    def __init__(self, pir_, led_):
        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)

        print pir_
        if pir_ is None:
            self.GPIO_PIR = pir_
        else:
            self.GPIO_PIR = 17

        print led_
        if led_ is None:
            self.GPIO_LED = led_
        else:
            self.GPIO_LED = 7

        print "PIR Module Test (CTRL-C to exit)"

        # Set pin as input
        GPIO.setup(self.GPIO_PIR, GPIO.IN)
        # Set up pin for LED
        GPIO.setup(self.GPIO_LED, GPIO.OUT)

        while GPIO.input(self.GPIO_PIR)==1:
            self.current_motion = 0

    def sense(self):
        print "Initiating PIR module"
        counter = 0
        camera = picamera.PiCamera()
        camera.vflip = True
        camera.hflip = False
        camera.brightness = 60

        try:

            # Loop until users quits with CTRL-C
            while True:

                # Read PIR state
                self.current_motion = GPIO.input(self.GPIO_PIR)

                if self.current_motion==1:
                    # TAKE A PHOTO
                    camera.start_preview()
                    camera.capture('image'+ str(counter) +'.jpg', format='jpeg')
                    camera.stop_preview()

                if self.current_motion==1 and self.previous_motion==0:
                    # PIR is triggered
                    print "  Motion detected! ("+ str(counter/100) +"s)"
                    counter = 0

                    # Turn on the LED
                    GPIO.output(self.GPIO_LED, True)
                    # Record previous state
                    self.previous_motion=1
                elif self.current_motion==0 and self.previous_motion==1:
                    # PIR has returned to ready state
                    print "  Waiting for Motion ("+ str(counter/100) +"s)"
                    counter = 0

                    # Turn off the LED
                    GPIO.output(self.GPIO_LED, False)
                    # Record previous state
                    self.previous_motion=0

                # Wait for 10 milliseconds
                time.sleep(0.01)
                counter += 1

        except KeyboardInterrupt:
            print "Quit"
            # Reset GPIO settings

        GPIO.cleanup()
