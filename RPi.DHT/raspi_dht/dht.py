#!/usr/bin/python

import Adafruit_DHT
from raspi_sensor.mqtt import MqttSensor


class Dht(MqttSensor):

    SENSOR = Adafruit_DHT.DHT22
    NAME = 'DHT'
    PIN = 21
    SLEEP = 10

    temperature = None
    humidity = None
    previous_temperature = None
    previous_humidity = None
    allowed_change = 10

    def setup_sensor(self):
        super().setup_sensor()

        if self.NAME in self.config:
            self.allowed_change = int(self.config.get(self.NAME, 'allowed_change', fallback=self.allowed_change))
            self.logger.debug('Sensor %s at allowed_change: %s', self.NAME, self.allowed_change)

    def setup_args(self, params):
        super().setup_args(params=params)

        if hasattr(params, 'allowed_change') and params.allowed_change:
            self.allowed_change = params.allowed_change
            self.logger.info('Sensor %s at allowed_change: %s (set by script parameter)', self.NAME,
                             self.allowed_change)

    def pre_sensor_read_callback(self):
        super().pre_sensor_read_callback()

        self.previous_temperature = self.temperature
        self.previous_humidity = self.humidity

    def sensor_read_callback(self):
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.SENSOR, self.PIN)
        self.logger.info('Sensor %s read data: %s *C and %s', self.NAME, self.temperature, self.humidity)

    def post_sensor_read_callback(self):
        if self.humidity is not None and self.temperature is not None:
            self.FAILED = 0

            difference = self.calculate_change_percentage(self.temperature, self.previous_temperature)

            if abs(difference) > self.allowed_change:
                self.FAILED = 1
                self.logger.warn('Sensor %s read data: %s *C which is difference %s % to previous reading %s *C',
                                 self.NAME, self.temperature, difference, self.previous_temperature)
            else:
                self.notify(topic='%s/temperature' % self.topic, payload="{0:0.1f}".format(self.temperature))

            difference = self.calculate_change_percentage(self.humidity, self.previous_humidity)

            if abs(difference) > self.allowed_change:
                self.FAILED = 1
                self.logger.warn('Sensor %s read data: %s % which is difference %s % to previous reading %s %',
                                 self.NAME, self.humidity, difference, self.previous_humidity)
            else:
                self.notify(topic='%s/humidity' % self.topic, payload="{0:0.1f}".format(self.humidity))
        else:
            self.FAILED += 1

        super().post_sensor_read_callback()

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
