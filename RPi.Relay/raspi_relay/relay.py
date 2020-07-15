#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
from raspi_sensor.sensor import Sensor


class Relay(Sensor):

    NAME = 'Relay'
    PIN = 11

    sensor_state = 0
    relay_state = 2  # Set unknown value, due to initial reading
    relay_closed = 0
    relay_open = 1

    def get_relay_state(self):
        if self.relay_state == self.relay_open:
            return 'Relay contact is open'
        else:
            return 'Relay contact is closed'

    def sensor_read_callback(self):
        self.sensor_state = self.GPIO.input(self.PIN)

    def post_sensor_read_callback(self):
        if self.sensor_state != self.relay_state:
            self.logger.debug('Sensor %s changing magnetic contact state from %s to %s', self.NAME, self.relay_state,
                              self.sensor_state)
            self.relay_state = self.sensor_state
            
            if self.relay_state:
                self.GPIO.output(self.PIN, 0)
            else:
                self.GPIO.output(self.PIN, 1)

            self.logger.info(self.get_relay_state())

        super().post_sensor_read_callback()
