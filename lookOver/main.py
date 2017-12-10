#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files, which you should have received as
# part of this distribution.

import sys
import os
import argparse
import textwrap
from lookOver import __version__ as VERSION, __description__ as DESCRIPTION
from lookOver import pir

PY3 = sys.version_info[0] > 2
# In order to make sure that Unicode is handled properly
# in Python 2.x, reset the default encoding.
if PY3:
    # noinspection PyUnresolvedReferences
    from configparser import RawConfigParser
else:
    from ConfigParser import RawConfigParser



def setup_args():
    ap = argparse.ArgumentParser(prog='lookOver',
            description='%(prog)s - ' + DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''\
                useful links:
                 - Wiki: https://github.com/ricco386/lookOver/wiki
                 - Bug Tracker: https://github.com/ricco386/lookOver/issues
                 - Twitter: https://twitter.com/ricco386

                author:
                  written by Richard Kellner (richard.kellner (at) erigones.com)

                license:
                  This software is licensed as described in the README.rst and LICENSE files,
                  which you should have received as part of this distribution.
                '''))
    # Sensors
    ap.add_argument('-p', '--pir', type=int, help='Set pin number on which is PIR sensor connected')
    ap.add_argument('--settle', action='store_true', help='Wait for PIR sensor to settle, before start')
    ap.add_argument('-l', '--led', type=int, help='Set pin number on which LED will be enabled when motion sensed')
    # Camera
    ap.add_argument('--width', type=int, help='Set camera resolution...')
    ap.add_argument('--height', type=int, help='Set camera resolution...')
    ap.add_argument('--nopicture', action='store_true', help='Disable picture at movement trigger')
    ap.add_argument('--novideo', action='store_true', help='Disable video recording at movement trigger')
    ap.add_argument('--hflip', action='store_true',
                    help='Retrieves of sets whether the renderer\'s output is horizontally flipped')
    ap.add_argument('--vflip', action='store_true',
                    help='Retrieves of sets whether the renderer\'s output is vertically flipped')
    ap.add_argument('--framerate', '-f', help='Set camera framerate...', nargs='?', default=False)
    # App
    ap.add_argument('-c', '--config', nargs='?', default=None, help='Path to configuration file that should be '
            'loaded to configure program')
    ap.add_argument('-ll', '--log_level', type=int, choices=[10, 20, 30, 40, 50],
            help="Set output verbosity (50: CRITICAL, 40: ERROR, 30: WARNING, 20: INFO, 10: DEBUG)")
    ap.add_argument('--version', action='version', version=('%(prog)s '+ VERSION))
    return ap.parse_args()

def setup_config(args):
    cfg_fp = None
    if args.config is not None:
        cfg_lo = ((args.config,),)
    else:
        cfg = 'lookOver.cfg'
        # Try to read config file from ~/.lookOver.cfg or /etc/lookOver.cfg
        cfg_lo = ((os.path.expanduser('~'), '.' + cfg), (sys.prefix, 'etc', cfg), ('/etc', cfg))

    for i in cfg_lo:
        try:
            cfg_fp = open(os.path.join(*i))
        except IOError:
            continue
        else:
            break

    #config_base_sections = ('global', 'camera')
    if not cfg_fp:
        sys.stderr.write("""\nLookOver can't start!\n
You need to create a config file in one this locations: \n%s\n
You can rename lookOver.cfg.example and update the required variables.
The example file is located in: %s\n\n""" % (
            '\n'.join([os.path.join(*i) for i in cfg_lo]),
            os.path.dirname(os.path.abspath(__file__))))
        sys.exit(1)

    # Read and parse configuration
    # noinspection PyShadowingNames
    def load_config(fp, reopen=False):
        config = RawConfigParser()
        if reopen:
            fp = open(fp.name)
        config.readfp(fp)
        fp.close()
        return config
    config = load_config(cfg_fp)

    #Merge parsed arguments into config
    for arg in args.__dict__.keys():
        if args.__getattribute__(arg) is not None:
            config.set('global', arg, args.__getattribute__(arg))

    if config.has_option('global', 'verbosity'):
        print config.get('global', 'verbosity')
    return config


def start():
    args = setup_args()
    lo = pir.Sensor(setup_config(args))
    lo.sense()

if __name__ == '__main__':
    start()
