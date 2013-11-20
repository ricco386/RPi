#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Richard Kellner

import pir

__version__ = '0.1dev'

def sense(pin_):
    return pir.Sensor.sense(pin_)

if __name__ == '__main__':
    pass
