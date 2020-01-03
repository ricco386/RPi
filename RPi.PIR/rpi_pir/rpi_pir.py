#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import time
from sensor import Sensor


class PIR(Sensor):

    NAME = 'PIR'
    PIN = 7

    sensor_state = 0
    previous_state = 0
    change_timestamp = 0.0
    change_delay = 30

    def settledown(self):
        self.logger.debug('Sensor %s waiting to settle down ...', self.NAME)
        # Loop until PIR output is 0
        while self.GPIO.input(self.PIN) == 1:
            self.sensor_state = 0

        self.logger.info('Sensor %s state is LOW.', self.NAME)

    def gpio_setup(self, gpio_bcm=False):
        super().gpio_setup(gpio_bcm)
        self.settledown()

    def pre_sensor_read_callback(self):
        super().pre_sensor_read_callback()
        # Record current sensor state for future comparasion
        self.previous_state = self.sensor_state

    def sensor_read_callback(self):
        # Read current sensor state
        self.sensor_state = self.GPIO.input(self.PIN)

    def post_sensor_read_callback(self):
        if self.sensor_state != self.previous_state:
            if self.change_timestamp < time.time() - self.change_delay:
                # Sensor change state time delay has passed, lets alert an event
                self.logger.info('Sensor %s state is %s.', self.NAME, "HIGH" if self.sensor_state else "LOW")
            else:
                self.change_timestamp = time.time()  # Reset the timestamp in order 
                self.sensor_state = self.previous_state  # Return to the state before reading

        super().post_sensor_read_callback()
