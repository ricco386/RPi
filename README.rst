RPi.Doorman
###########

Door state monitor, completely written in Python.

.. image:: https://badge.fury.io/py/rpi-doorman.png
    :target: http://badge.fury.io/py/rpi-doorman

Doorman is using adafruit magnetic contact switch (door sensor), with Raspberry Pi GPIO. Software might work with other sensors as well but have not been tested.

To connect to Raspberry Pi plug into GPIO PIN 16 and POWER PIN. Install and execute doorman and it should work. Alternatively you can user different PIN and execute doorman with parameter: ``rpi-doorman --pin pin_number``.

Doorman has support to POST door status change to `ludolph-doorman <https://github.com/ricco386/ludolph-doorman/>`_ plugin. This way jabber notifications can be set easily.

Installation
------------

- Install the latest released version using pip::

      pip install https://github.com/ricco386/rpi-doorman/zipball/master

- Make sure all dependencies (listed below) are installed (done automatically when installing via pip)
- The ``rpi-doorman`` command should be installed somewhere in your ``PATH``.
- Systemd scripts are available: https://github.com/ricco386/rpi-doorman/tree/master/init.d

Systemd scripts should be run under **default Raspberry Pi user** (pi) so scripts can access GPIO. 

For jabber notification support, configure Systemd to execute with notify parameter: ``rpi-doorman --notify jabber@account.com`` make sure `Ludolph <https://github.com/erigones/Ludolph/>`_ is installed and has configured `ludolph-doorman <https://github.com/ricco386/ludolph-doorman/>`_ plugin. 

**Dependencies:**

- `RPi.GPIO <https://pypi.python.org/pypi/RPi.GPIO>`_ (0.6.1+)

Optionaly dependencies for jabber support:

- `requests <https://pypi.python.org/pypi/requests>`_ (2.9.1+)
- `ludolph-doorman <https://github.com/ricco386/ludolph-doorman/>`_ (1.1+)


License
-------

For more information see the `LICENSE <https://github.com/ricco386/rpi-doorman/blob/master/LICENSE>`_ file.
