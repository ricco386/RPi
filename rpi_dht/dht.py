#!/usr/bin/python

import sys
import Adafruit_DHT
import argparse
from sensor import Sensor, Setup


class Dht(Sensor):

    NAME = 'DHT'
    SENSOR = Adafruit_DHT.DHT22
    sensor_pin = 21
    temperature = None
    humidity = None
    display_temp = False
    display_hum = False

    def __init__(self, args=[]):
        super(Dht, self).__init__(args)

        if args:
            if hasattr(args, 't') and args.t:
                self.display_temp = args.t
            if hasattr(args, 'hu') and args.hu:
                self.display_hum = args.hu

    def __str__(self):
        self.output()

    def sensor_read(self):
        super(Dht, self).sensor_read()
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.SENSOR, self.sensor_pin)

    def output(self):
        # Note that sometimes you won't get a reading and the results will be null
        # (because Linux can't guarantee the timing of calls to read the sensor).
        # If this happens try again!
        out = ''

        if self.humidity is not None and self.temperature is not None:
            if self.display_temp:
                out += 'Temp={0:0.1f}*C '.format(self.temperature)
            if self.display_hum:
                out += 'Humidity={0:0.1f}%'.format(self.humidity)
            if not self.display_temp and not self.display_hum:
                out = 'No value to read defined!'
        else:
            out = 'Failed to get reading. Try again!'

        return out


class DhtSetup(Setup):

    def args(self, name, desc):
        ap = super(DhtSetup, self).args(name, desc)
        ap.add_argument('-t', action='store_true', help='Show temperature.')
        ap.add_argument('-hu', action='store_true', help='Show humidity.')

        return ap
