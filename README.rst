# Doorman

Door state monitor, completely written in Python.

Doorman is using adafruit magnetic contact switch (door sensor), with Raspberry Pi GPIO. Software might work with other sensors as well but have not been tested.

To connect to Raspberry Pi plug into GPIO PIN 18 and POWER PIN. Install and execute doorman and it should work.


Installation
------------

- Install the latest released version using pip::

      pip install https://github.com/ricco386/doorman/zipball/master

- Make sure all dependencies (listed below) are installed (done automatically when installing via pip)
- The ``doorman`` command should be installed somewhere in your ``PATH``.
- Systemd scripts are available: https://github.com/ricco386/doorman/tree/master/init.d

**Dependencies:**

- `RPi.GPIO <https://pypi.python.org/pypi/RPi.GPIO>`_ (0.6.1+)

License
-------

For more information see the `LICENSE <https://github.com/ricco386/doorman/blob/master/LICENSE>`_ file.
