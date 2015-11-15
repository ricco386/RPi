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
            if args.p:
                self.PIN = args.p
            if args.t:
                self.TEMP = args.t
            if args.hu:
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

        if args.pa:
            self.LOG_PATH = args.pa

        logging.basicConfig(filename=self.LOG_PATH, level=logging.INFO)
        super(DhtDaemon, self).__init__(pidfile)

    def run(self):
        sensor = Dht(self.args)
        while True:
            logging.info(sensor.output())
            time.sleep(10)


def setup_args():
    ap = argparse.ArgumentParser(prog='DHTtemp')
    ap.add_argument('-t', action='store_true', help='show temperature')
    ap.add_argument('-hu', action='store_true', help='show humidity')
    ap.add_argument('-p', type=int, help='set DHT sensor pin')
    ap.add_argument('-pa', type=str, help='set path where log will be stored')
    ap.add_argument('-d', type=str, help='daemon mode, usage: start|stop|restart')


    return ap.parse_args()


if __name__ == '__main__':
    args = setup_args()

    if args.d:
        daemon = DhtDaemon('/tmp/dht.pid', args)
        if args.d in ('start', 'stop', 'restart'):
            if 'start' == args.d:
                daemon.start()
            elif 'stop' == args.d:
                daemon.stop()
            elif 'restart' == args.d:
                daemon.restart()
            else:
                print("Unknown command")
                sys.exit(2)
            sys.exit(0)
        else:
            print("usage: %s start|stop|restart" % args.d)
            sys.exit(2)
    else:
        sensor = Dht(args)
        print(sensor.output())
        sys.exit(0)
