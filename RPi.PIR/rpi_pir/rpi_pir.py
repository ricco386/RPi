#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
from sensor import Sensor


class PIR(Sensor):

    NAME = 'PIR'
    PIN = 21

    sensor_state = 0
    previous_state = 0

    def settledown(self):
        self.logger.debug('Sensor %s waiting to settle down ...', self.NAME)
        # Loop until PIR output is 0
        while self.GPIO.input(self.PIN)==1:
            self.sensor_state = 0

        self.logger.debug('... Ready!')

    def gpio_setup(self, gpio_bcm=False):
        super().gpio_setup(gpio_bcm)
        self.settledown()

    def sensor_read_callback(self):
        self.previous_state = self.sensor_state
        self.sensor_state = self.GPIO.input(self.PIN)

        if self.sensor_state != self.previous_state:
            self.logger.debug('Sensor %s state is %s.', self.NAME, "HIGH" if self.sensor_state else "LOW")