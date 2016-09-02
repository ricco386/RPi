#!/usr/bin/python

import sys
import Adafruit_DHT
import argparse
from sensor import Sensor


class Dht(Sensor):

    SENSOR = Adafruit_DHT.DHT22
    NAME = 'DHT'

    cycle_sleep = 10

    temperature = None
    humidity = None

    def __init__(self, args=[]):
        super(Dht, self).__init__(args)
        self.logger.info('At your service')

    def __str__(self):
        self.output()

    def set_gpio(self):
        return

    def sensor_cleanup(self):
        return

    def sensor_read_callback(self):
        super(Dht, self).sensor_read_callback()
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(self.SENSOR, self.sensor_pin)
        self.logger.info('Data from sensor: %s *C and %s' % (temperature, humidity))

        if humidity is not None and temperature is not None:

            humidity = round(humidity, 2)
            if self.humidity != humidity:
                self.humidity = humidity

                if self.config.has_option('server', 'hostname'):
                    self.post_data('api/measurements/', self.generate_post_dict(humidity, 2))

            temperature = round(temperature, 2)
            if self.temperature != temperature:
                self.temperature = temperature

                if self.config.has_option('server', 'hostname'):
                    self.post_data('api/measurements/', self.generate_post_dict(temperature, 1))

            self.failed = 0
        else:
            self.failed += 1

    def generate_post_dict(self, value, unit):
        return {
            'node': self.config.get('global', 'node_id'),
            'sensor': self.config.get(self.NAME, 'sensor_id'),
            'value': value,
            'unit': unit,
        }

    def output(self, desc=True, temp=False, hum=False):
        self.logger.debug('Starting onetime sense process...')
        self.sensor_setup()

        # Note that sometimes you won't get a reading and the results will be null
        # (because Linux can't guarantee the timing of calls to read the sensor).
        # If this happens try again!
        self.sensor_read()
        out = ''

        if desc and (self.temperature or self.humidity):
            out += 'Temperature = {0:0.1f}*C\n'.format(self.temperature)
            out += 'Humidity = {0:0.1f}%'.format(self.humidity)
        else:
            out = 'Failed to get reading. Try again!'

        if temp and self.temperature:
            out = str(self.temperature)

        if hum and self.humidity:
            out = str(self.humidity)

        return out
