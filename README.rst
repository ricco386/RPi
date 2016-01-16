RPi.Doorman
###########

Door state monitor, completely written in Python.

.. image:: https://badge.fury.io/py/rpi-doorman.png
    :target: http://badge.fury.io/py/rpi-doorman

Doorman is using adafruit magnetic contact switch (door sensor), with Raspberry Pi GPIO. Software might work with other sensors as well but have not been tested.

To connect to Raspberry Pi plug into GPIO PIN 16 and POWER PIN. Install and execute doorman and it should work. Alternatively you can user different PIN and execute doorman with parameter: ``doorman --pin pin_number``.


Installation
------------

- Install the latest released version using pip::

      pip install https://github.com/ricco386/rpi-doorman/zipball/master

- Make sure all dependencies (listed below) are installed (done automatically when installing via pip)
- The ``doorman`` command should be installed somewhere in your ``PATH``.
- Systemd scripts are available: https://github.com/ricco386/rpi-doorman/tree/master/init.d

**Dependencies:**

- `RPi.GPIO <https://pypi.python.org/pypi/RPi.GPIO>`_ (0.6.1+)
- `requests <https://pypi.python.org/pypi/requests>`_ (2.9.1+)

License
-------

For more information see the `LICENSE <https://github.com/ricco386/rpi-doorman/blob/master/LICENSE>`_ file.
