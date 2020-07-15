RPi.Relay
#########

Relay state operator, completely written in Python.

RPi.Relay can change relay state, via Raspberry Pi GPIO.

To connect to Raspberry Pi plug into GPIO PIN 11 (default) and POWER PIN. Install and execute raspi-relay and it should work. Alternatively you can user different PIN and execute raspi-relay with parameter: ``raspi-relay --pin pin_number``.

Pre-Installation requirements
-----------------------------

- Update system and install required dependencies::

    sudo apt-get update
    sudo apt-get install build-essential python3-dev python3-pip

Installation
------------

- Clone repository::

    git clone git@github.com:ricco386/RPi.git

- Go to RPi.Relay directory::

    cd RPi.Relay

- Install the latest released version using pip::

    python3 -m pip install --upgrade .

- Make sure all dependencies (listed below) are installed (done automatically when installing via pip)
- The ``raspi-relay`` command should be installed somewhere in your ``PATH`` (done automatically when installing via pip), make sure `raspi-relay.service` has corect path in `ExecStart` set to `raspi-relay` executable.
- Systemd scripts are available: https://github.com/ricco386/RPi/tree/master/RPi.Relay/init.d to install them you will need root privileges, so we execute them as sudo::

    sudo cp init.d/raspi-relay.conf /etc/tmpfiles.d/
    sudo cp init.d/raspi-relay.service /etc/systemd/system/
    sudo systemd-tmpfiles --create /etc/tmpfiles.d/raspi-relay.conf
    sudo systemctl enable raspi-relay.service  # Enable service to start at system boot
    sudo systemctl start raspi-relay.service  # Start

Systemd scripts should be run under **default Raspberry Pi user** (pi), scripts have to be able access GPIO.

**Dependencies:**

- `RPi.Sensor <https://pypi.python.org/pypi/RPi.Sensor>`_ (0.5.2+)

Usage
-----

You have to create a `.sensor.cfg` file and place into `/home/pi/.sensor.cfg` you can find example file in RPi.Sensor repo: https://github.com/ricco386/RPi.Sensor/blob/master/sensor.cfg.example and add values in `[Relay]` section.

`raspi-relay` support parameters to overwrite config parameters. For more info run::

    raspi-relay --help


License
-------

For more information see the `LICENSE <https://github.com/ricco386/RPi/blob/master/RPi.Relay/LICENSE>`_ file.
