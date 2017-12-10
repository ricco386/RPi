lookOver
========

Raspberry Pi application for recording pictures/videos with PiCamera when motion is detected by PIR sensor.


Installation Notes
------------------

 - Install the latest released version using pip::

    pip install lookOver

 - Make sure all dependencies (listed below) are installed (done automatically when installing via pip)

 - Create and edit the config file::

    cp /usr/lib/python2.7/site-packages/lookOver/lookOver.cfg.example /etc/lookOver.cfg

 - The ``lo`` command should be installed somewhere in your ``PATH``.

 - Init scripts for Debian based distributions is available: https://github.com/ricco386/lookOver/tree/master/init.d


**Dependencies:**
 - RPi.GPIO
 - picamera
 - colorama

Useful Links
------------

 - Wiki: https://github.com/ricco386/lookOver/wiki
 - Bug Tracker: https://github.com/ricco386/lookOver/issues
 - Twitter: https://twitter.com/ricco386

License
-------

For more informations see the LICENSE file.
