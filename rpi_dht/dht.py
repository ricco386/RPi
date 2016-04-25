#!/usr/bin/python

import sys
import Adafruit_DHT
import argparse
from sensor import Sensor, Setup


class Dht(Sensor):

    SENSOR = Adafruit_DHT.DHT22
    NAME = 'DHT'
    sensor_pin = 21
    cycle_sleep = 10

    data = None
    nofity = True

    def __init__(self, args=[]):
        super(Dht, self).__init__(args)

        self.data = {
            'humidity': None,
            'temperature': None,
        }

    def __str__(self):
        self.output()

    def sensor_read_callback(self):
        super(Dht, self).sensor_read_callback()
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(self.SENSOR, self.sensor_pin)
        self.log.info('Data from sensor: %s *C and %s' % (temperature, humidity))

        if humidity is not None and temperature is not None:
            if data['humidity'] != humidity:
                data['humidity'] = humidity
                self.post_data(self.generate_post_dict(self, humidity, 2))

            if data['temperature'] != temperature:
                data['temperature'] = temperature
                self.post_data((self.generate_post_dict(self, temperature, 1))

            self.failed = 0
        else:
            self.failed += 1

    def generate_post_dict(self, value, unit):
        # TODO: hardcoded values, BAD! Re-write in better way.
        return {
            'node': 1,
            'sensor': 1,
            'value': value,
            'unit': unit,
        }

    def output(self):
        # Note that sometimes you won't get a reading and the results will be null
        # (because Linux can't guarantee the timing of calls to read the sensor).
        # If this happens try again!
        out = ''

        if self.data:
            out += 'Temperature = {0:0.1f}*C '.format(self.data['temperature'])
            out += 'Humidity = {0:0.1f}%'.format(self.data['humidity'])
        else:
            out = 'Failed to get reading. Try again!'

        return out
