#!/usr/bin/python

import Adafruit_DHT
from sensor import Sensor


class Dht(Sensor):

    SENSOR = Adafruit_DHT.DHT22
    NAME = 'DHT'
    PIN = 21
    SLEEP = 10

    temperature = None
    humidity = None

    def gpio_setup(self, gpio_bcm=False):
        pass

    def gpio_cleanup(self):
        pass

    def sensor_read_callback(self):
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.SENSOR, self.PIN)
        self.logger.info('Sensor %s read data: %s *C and %s', self.NAME, self.temperature, self.humidity)

        if self.humidity is not None and self.temperature is not None:
            self.FAILED = 0
        else:
            self.FAILED += 1

    def output(self, desc=True, temp=False, hum=False):
        # Note that sometimes you won't get a reading and the results will be null
        # (because Linux can't guarantee the timing of calls to read the sensor).
        # If this happens try again!
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
