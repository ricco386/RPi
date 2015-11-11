#!/usr/bin/python

import Adafruit_DHT
import argparse

SENSOR = Adafruit_DHT.DHT22
DEFAULT_PIN = 27

def setup_args():
    ap = argparse.ArgumentParser(prog='DHTtemp')
    ap.add_argument('-t', action='store_true', help='show temperature')
    ap.add_argument('-hu', action='store_true', help='show humidity')
    ap.add_argument('-p', type=int, help='set DHT sensor pin')
    return ap.parse_args()

def start():
    args = setup_args()

    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    pin = DEFAULT_PIN
    if args.p:
        pin = args.p
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, pin)

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
        # print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
        if args.t:
            print(temperature)
        if args.hu:
            print(humidity)
        if not args.hu and not args.t:
            print('You havent provided any parameter try --help')
    else:
        print('Failed to get reading. Try again!')


if __name__ == '__main__':
    start()
