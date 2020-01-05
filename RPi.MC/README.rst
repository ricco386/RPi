RPi.MC
######

Magnetic contact state monitor, completely written in Python.

RPi.MC is using adafruit magnetic contact switch (door/window sensor), with Raspberry Pi GPIO. Software might work with other sensors as well but have not been tested.

To connect to Raspberry Pi plug into GPIO PIN 11 and POWER PIN. Install and execute raspi-mc and it should work. Alternatively you can user different PIN and execute raspi-mc with parameter: ``raspi-mc --pin pin_number``.

Installation
------------

- Clone repository::

    git clone git@github.com:ricco386/RPi.git

- Go to RPi.MC directory::

    cd RPi.MC

- Install the latest released version using pip::

    python3 -m pip install .

- Make sure all dependencies (listed below) are installed (done automatically when installing via pip)
- The ``raspi-mc`` command should be installed somewhere in your ``PATH`` (done automatically when installing via pip), make sure `raspi-mc.service` has corect path in `ExecStart` set to `raspi-mc` executable.
- Systemd scripts are available: https://github.com/ricco386/RPi/tree/master/RPi.PIR/init.d to install them you will need root privileges, so we execute them as sudo::

    sudo cp init.d/raspi-mc.conf /etc/tmpfiles.d/
    sudo cp init.d/raspi-mc.service /etc/systemd/system/
    sudo systemd-tmpfiles --create /etc/tmpfiles.d/raspi-mc.conf
    sudo systemctl enable raspi-mc.service  # Enable service to start at system boot
    sudo systemctl start raspi-mc.service  # Start

Systemd scripts should be run under **default Raspberry Pi user** (pi), scripts have to be able access GPIO.

**Dependencies:**

- `RPi.Sensor <https://pypi.python.org/pypi/RPi.Sensor>`_ (0.3.0+)

Usage
-----

You have to create a `.sensor.cfg` file and place into `/home/pi/.sensor.cfg` you can find example file in RPi.Sensor repo: https://github.com/ricco386/RPi.Sensor/blob/master/sensor.cfg.example and override values in `[Magnetic_Contact]` section.

`raspi-mc` also support parameters to overwrite config parameters. For more info run::

    raspi-mc --help

License
-------

For more information see the `LICENSE <https://github.com/ricco386/RPi/blob/master/RPi.MC/LICENSE>`_ file.
