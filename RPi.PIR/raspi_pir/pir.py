#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import time

from raspi_sensor.sensor import Sensor
from raspi_sensor.zabbix import zabbix_sender


class PIR(Sensor):

    NAME = 'PIR'
    TRAPPER = 'rpi.pir-state'
    PIN = 7

    sensor_state = 0
    previous_state = 0
    change_delay = 60
    last_high = 0.0
    low_notif = True

    def settledown(self):
        self.logger.debug('Sensor %s waiting to settle down ...', self.NAME)
        # Loop until PIR output is 0
        while self.GPIO.input(self.PIN) == 1:
            self.sensor_state = 0

        self.logger.info('Sensor %s state is LOW.', self.NAME)
        self.notify(topic='%s/status' % self.mqtt_topic, payload=self.sensor_state)

    def gpio_setup(self):
        super().gpio_setup()
        self.settledown()

    def pre_sensor_read_callback(self):
        super().pre_sensor_read_callback()
        # Record current sensor state for future comparison
        self.previous_state = self.sensor_state

    def sensor_read_callback(self):
        # Read current sensor state
        self.sensor_state = self.GPIO.input(self.PIN)

    def post_sensor_read_callback(self):
        if self.sensor_state != self.previous_state:
            self.logger.info('Sensor %s state is %s.', self.NAME, "HIGH" if self.sensor_state else "LOW")

            if self.sensor_state:
                self.last_high = time.time()
                self.low_notif = True

                self.notify(topic='%s/status' % self.mqtt_topic, payload=self.sensor_state)
                zabbix_sender(self.config, self.TRAPPER, self.sensor_state)
                self.logger.debug('Sensor %s sent zabbix_sender trapper item %s with value %s.', self.NAME,
                                  self.TRAPPER, self.sensor_state)

        if not self.sensor_state and self.last_high < time.time() - self.change_delay and self.low_notif:
            self.low_notif = False

            self.notify(topic='%s/status' % self.mqtt_topic, payload=self.sensor_state)
            zabbix_sender(self.config, self.TRAPPER, self.sensor_state)
            self.logger.debug('Sensor %s sent zabbix_sender trapper item %s with value %s.', self.NAME, self.TRAPPER,
                              self.sensor_state)

        super().post_sensor_read_callback()
