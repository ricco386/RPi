RPi.MC
######

Magnetic contact state monitor, completely written in Python.

RPi.MC is using adafruit magnetic contact switch (door/window sensor), with Raspberry Pi GPIO. Software might work with other sensors as well but have not been tested.

To connect to Raspberry Pi plug into GPIO PIN 11 and POWER PIN. Install and execute raspi-mc and it should work. Alternatively you can user different PIN and execute raspi-mc with parameter: ``raspi-mc --pin pin_number``.

Installation
------------

- Install the latest released version using pip::

    python3 -m pip install -e git+https://github.com/ricco386/RPi.git#egg=version_subpkg&subdirectory=RPi.MC

- Make sure all dependencies (listed below) are installed (done automatically when installing via pip)
- The ``raspi-mc`` command should be installed somewhere in your ``PATH``.
- Systemd scripts are available: https://github.com/ricco386/RPi/tree/master/RPi.PIR/init.d

Systemd scripts should be run under **default Raspberry Pi user** (pi), scripts have to be able access GPIO.

**Dependencies:**

- `RPi.Sensor <https://pypi.python.org/pypi/RPi.Sensor>`_ (0.3.0+)

License
-------

For more information see the `LICENSE <https://github.com/ricco386/RPi/blob/master/RPi.PIR/LICENSE>`_ file.
