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

    def __init__(self, args):
        self.out = Output(args)
        self.args = args

        if not self.args.nopicture or not self.args.novideo:
            self.camera = picamera.PiCamera()

            if self.args.hflip:
                self.camera.hflip = True
            if self.args.vflip:
                self.camera.vflip = True
            if self.args.width and self.args.height:
                self.camera.resolution = (self.args.width, self.args.height)
            if self.args.framerate:
                self.camera.framerate = self.args.framerate

    def getFileName(self, extension='.h264'):
        directory = self.out.getDir()
        time = str(datetime.datetime.now().strftime("%H_%M_%S"))
        return directory + time + extension

    def start_recording(self):
        self.out.msg('Initiating recording', DEBUG)
        if not self.args.nopicture:
            fileName = self.getFileName(extension='.jpg')
            self.out.msg('Picture preview', DEBUG)
            self.camera.start_preview()
            self.out.msg('Picture capture: %s' % fileName, DEBUG)
            self.camera.capture(fileName)
            self.out.msg('Picture captured', INFO)
        if not self.args.novideo:
            fileName = self.getFileName()
            self.out.msg('Video preview', DEBUG)
            self.camera.start_preview()
            self.out.msg('Video recording: %s' % fileName, DEBUG)
            self.camera.start_recording(fileName)

    def stop_recording(self):
        if not self.args.novideo:
            self.camera.stop_preview()
            self.camera.stop_recording()
            self.out.msg('Video recorded', INFO)
        self.out.msg('Finished recording', DEBUG)
