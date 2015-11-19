#!/usr/bin/python

import sys
import time
import logging
import Adafruit_DHT
import argparse
from daemon3 import Daemon


class Dht(object):
    SENSOR = Adafruit_DHT.DHT22
    PIN = 27
    TEMP = False
    HUM = False

    def __init__(self, args=None):
        if args:
            if hasattr(args, 'p') and args.p:
                self.PIN = args.p
            if hasattr(args, 't') and args.t:
                self.TEMP = args.t
            if hasattr(args, 'hu') and args.hu:
                self.HUM = args.hu

    def sense(self):
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        return Adafruit_DHT.read_retry(self.SENSOR, self.PIN)

    def output(self):
        humidity, temperature = self.sense()

        # Note that sometimes you won't get a reading and the results will be null
        # (because Linux can't guarantee the timing of calls to read the sensor).
        # If this happens try again!
        if humidity is not None and temperature is not None:
            out = ''
            if self.TEMP:
                out += 'Temp={0:0.1f}*C '.format(temperature)
            if self.HUM:
                out += 'Humidity={0:0.1f}%'.format(humidity)
            if not self.TEMP and not self.HUM:
                out = 'No value to read defined!'
        else:
            out = 'Failed to get reading. Try again!'

        return out


class DhtDaemon(Daemon):
    LOG_PATH = '/tmp/dht.log'

    def __init__(self, pidfile, args=None):
        self.args = args

        if hasattr(args, 'l') and args.l:
            self.LOG_PATH = args.l

        logging.basicConfig(filename=self.LOG_PATH, level=logging.INFO)
        super(DhtDaemon, self).__init__(pidfile)

    def run(self):
        sensor = Dht(self.args)
        while True:
            logging.info(sensor.output())
            time.sleep(10)


def setup_args():
    ap = argparse.ArgumentParser(prog='DHTtemp')
    ap.add_argument('-t', action='store_true', help='Show temperature.')
    ap.add_argument('-hu', action='store_true', help='Show humidity.')
    ap.add_argument('-p', type=int, help='Set DHT sensor pin.')
    ap.add_argument('-d', type=str, help='Run in daemon mode. Usage: [start|stop|restart]')
    ap.add_argument('-l', type=str, help='Path where log will be stored. Used only in daemon mode.')

    return ap.parse_args()


if __name__ == '__main__':
    args = setup_args()

    if hasattr(args, 'd') and args.d:
        daemon = DhtDaemon('/tmp/dht.pid', args)
        if args.d in ('start', 'stop', 'restart'):
            if 'start' == args.d:
                daemon.start()
            elif 'stop' == args.d:
                daemon.stop()
            elif 'restart' == args.d:
                daemon.restart()
            sys.exit(0)
        else:
            print("DHTtemp: error: argument -d: usage [start|stop|restart]")
            sys.exit(2)
    else:
        sensor = Dht(args)
        print(sensor.output())
        sys.exit(0)
