#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import picamera
import datetime
from logging import WARNING, INFO
import os
import logging
import subprocess
from argparse import ArgumentParser
from lookOver.out import Output


class Camera():
    args = None
    camera = None
    out = None
    today = None
    path = None

    def __init__(self, args):
        self.out = Output(args)
        self.args = args
        self.camera = picamera.PiCamera()
        self.today = str(datetime.datetime.now().strftime("%Y-%m-%d"))

        if self.args.hflip:
            self.camera.hflip = True
        if self.args.vflip:
            self.camera.vflip = True

    def getDir(self, date):
        if self.path is None:
            hddcko_path = '/mnt/hddcko/pictures'
            if not os.path.ismount(hddcko_path):
                self.out.msg('%s is not mounted, try to mount' % hddcko_path, WARNING)
                subprocess.call(["mount", hddcko_path])
                if not os.path.ismount(hddcko_path):
                    self.out.msg('Couldnt mount %s' % hddcko_path, WARNING)
                    hddcko_path = '/home/pi'
                else:
                    self.out.msg('Yey %s has been mounted' % hddcko_path, INFO)

            self.path = hddcko_path + '/lookOver/' + date +'/'
            if not os.path.exists(self.path):
                self.out.msg('Creating directory %s' % self.path, INFO)
                os.mkdir(self.path)

        return self.path

    def getFileName(self, extension='.h264'):
        directory = self.getDir(self.today)
        time = str(datetime.datetime.now().strftime("%H.%M.%S"))
        return directory + time + extension

    def start_recording(self):
        self.out.msg('Start recording')
        #if self.test:
        #    return
        # Take photo
        fileName = self.getFileName(extension='.jpg')
        self.camera.start_preview()
        self.camera.capture(fileName)
        # Start recording
        t = time.time()
        fileName = self.getFileName()
        self.camera.start_preview()
        self.camera.start_recording(fileName)

    def stop_recording(self):
        self.out.msg('Stopped recording')
        #if self.test:
        #    return
        self.camera.stop_preview()
        self.camera.stop_recording()
