#!/usr/bin/python

import sys
import Adafruit_DHT
import argparse
from sensor import Sensor, Setup


class Dht(Sensor):

    SENSOR = Adafruit_DHT.DHT22
    NAME = 'DHT'
    sensor_pin = 21

    temperature = None
    humidity = None
    data = None

    def __str__(self):
        self.output()

    def sensor_read(self):
        super(Dht, self).sensor_read()
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(self.SENSOR, self.sensor_pin)

        if humidity is not None and temperature is not None:
            self.data = {
                'humidity': humidity,
                'temperature': temperature,
            }

    def post_sensor_check(self):
        super(Dht, self).post_sensor_check()

        if self.url:
            self.post_data(self.data)

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
