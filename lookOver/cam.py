#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files, which you should have received as
# part of this distribution.

import picamera
import datetime
from logging import INFO, DEBUG
from lookOver.out import Output


class Camera():
    args = None
    camera = None
    out = None
    today = None

    def __init__(self, args):
        self.out = Output(args)
        self.args = args

        if not self.args.nopicture or not self.args.novideo:
            self.camera = picamera.PiCamera()
            self.today = str(datetime.datetime.now().strftime("%Y-%m-%d"))

            if self.args.hflip:
                self.camera.hflip = True
            if self.args.vflip:
                self.camera.vflip = True

    def getFileName(self, extension='.h264'):
        directory = self.out.getDir(self.today)
        time = str(datetime.datetime.now().strftime("%H_%M_%S"))
        return directory + time + extension

    def start_recording(self):
        self.out.msg('Initiating recording', DEBUG)
        if not self.args.nopicture:
            fileName = self.getFileName(extension='.jpg')
            self.out.msg('Picture preview: %s' % fileName, DEBUG)
            self.camera.start_preview()
            self.camera.capture(fileName)
            self.out.msg('Picture crated', INFO)
        if not self.args.novideo:
            fileName = self.getFileName()
            self.out.msg('Video preview: %s' % fileName, DEBUG)
            self.camera.start_preview()
            self.camera.start_recording(fileName)

    def stop_recording(self):
        if not self.args.novideo:
            self.camera.stop_preview()
            self.camera.stop_recording()
            self.out.msg('Video created', INFO)
        self.out.msg('Finished recording', DEBUG)
