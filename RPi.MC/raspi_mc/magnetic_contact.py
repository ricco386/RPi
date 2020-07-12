#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
from raspi_sensor.mqtt import MqttSensor
from raspi_sensor.zabbix import zabbix_sender


class MC(MqttSensor):

    NAME = 'Magnetic_Contact'
    TRAPPER = 'rpi.mc-state'
    PIN = 11

    sensor_state = 0
    door_state = 2  # Set unknown value, due to initial reading
    door_closed = 0
    door_open = 1

    def get_door_state(self):
        if self.door_state == self.door_open:
            return 'Magnetic contact is open'
        else:
            return 'Magnetic contact is closed'

    def sensor_read_callback(self):
        self.sensor_state = self.GPIO.input(self.PIN)

    def post_sensor_read_callback(self):
        if self.sensor_state != self.door_state:
            self.logger.debug('Sensor %s changing magnetic contact state from %s to %s', self.NAME, self.door_state,
                              self.sensor_state)
            self.door_state = self.sensor_state
            self.logger.info(self.get_door_state())

            self.notify(topic='%s/status' % self.topic, payload=self.sensor_state)
            zabbix_sender(self.config, self.TRAPPER, self.sensor_state)
            self.logger.debug('Sensor %s sent zabbix_sender trapper item %s with value %s.', self.NAME, self.TRAPPER,
                              self.sensor_state)

        super().post_sensor_read_callback()
