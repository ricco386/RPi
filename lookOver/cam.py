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
    cfg = None
    camera = None
    out = None

    def __init__(self, config):
        self.out = Output(config)
        self.cfg = config

        self.camera = picamera.PiCamera()
        self.camera.hflip = config.get('global', 'hflip')
        self.camera.vflip = config.get('global', 'vflip')
        self.camera.resolution = (config.getint('global', 'width'),config.getint('global', 'height'))

    def getFileName(self, extension='.h264'):
        directory = self.out.getDir()
        time = str(datetime.datetime.now().strftime("%H_%M_%S"))
        return directory + time + extension

    def capture_image(self):
        fileName = self.getFileName(extension='.jpg')
        self.out.msg('Picture preview', DEBUG)
        self.camera.start_preview()
        self.out.msg('Picture capture: %s' % fileName, DEBUG)
        self.camera.capture(fileName)
        self.out.msg('Picture captured', INFO)

    def capture_sequence(self):
        fileName = self.getFileName(extension='__{counter:03d}.jpg')
        self.out.msg('Picture sequence preview', DEBUG)
        self.camera.start_preview()
        self.out.msg('Picture sequence recording: %s' % fileName, DEBUG)
        self.camera.capture_continuous(fileName)

    def capture_video(self):
        fileName = self.getFileName()
        self.out.msg('Video preview', DEBUG)
        self.camera.start_preview()
        self.out.msg('Video recording: %s' % fileName, DEBUG)
        self.camera.start_recording(fileName)


    def start_recording(self):
        self.out.msg('Initiating recording', DEBUG)

        if self.cfg.get('global', 'type') == 'image':
            self.capture_image()
        if self.cfg.get('global', 'type') == 'image_sequence':
            self.capture_squence()
        if self.cfg.get('global', 'type') == 'video':
            self.capture_video()

    def stop_recording(self):
        if self.cfg.get('global', 'type') in ('image_sequence', 'video'):
            self.camera.stop_preview()
            self.camera.stop_recording()
            self.out.msg('Finished recording', INFO)
