RPi.PIR
#######

PIR sensor state monitor, completely written in Python.

RPi.PIR is using PIR sensor with Raspberry Pi GPIO. Software might work with other sensors as well but have not been tested.

To connect to Raspberry Pi plug into GPIO PIN 11 and POWER PIN. Install and execute raspi-pir and it should work. Alternatively you can user different PIN and execute raspi-pir with parameter: ``raspi-pir --pin pin_number``.

Pre-Installation requirements
-----------------------------

- Update system and install required dependencies::

    sudo apt-get update
    sudo apt-get install build-essential python3-dev python3-pip

Installation
------------

- Clone repository::

    git clone git@github.com:ricco386/RPi.git

- Go to RPi.PIR directory::

    cd RPi.PIR

- Install the latest released version using pip::

    python3 -m pip install --upgrade .

- Make sure all dependencies (listed below) are installed (done automatically when installing via pip)
- The ``raspi-pir`` command should be installed somewhere in your ``PATH`` (done automatically when installing via pip), make sure `raspi-pir.service` has corect path in `ExecStart` set to `raspi-pir` executable.
- Systemd scripts are available: https://github.com/ricco386/RPi/tree/master/RPi.PIR/init.d to install them you will need root privileges, so we execute them as sudo::

    sudo cp init.d/raspi-pir.conf /etc/tmpfiles.d/
    sudo cp init.d/raspi-pir.service /etc/systemd/system/
    sudo systemd-tmpfiles --create /etc/tmpfiles.d/raspi-pir.conf
    sudo systemctl enable raspi-pir.service  # Enable service to start at system boot
    sudo systemctl start raspi-pir.service  # Start

Systemd scripts should be run under **default Raspberry Pi user** (pi), scripts have to be able access GPIO.

**Dependencies:**

- `RPi.Sensor <https://pypi.python.org/pypi/RPi.Sensor>`_ (0.3.0+)

Usage
-----

You have to create a `.sensor.cfg` file and place into `/home/pi/.sensor.cfg` you can find example file in RPi.Sensor repo: https://github.com/ricco386/RPi.Sensor/blob/master/sensor.cfg.example and override values in `[PIR]` section.

`raspi-pir` also support parameters to overwrite config parameters. For more info run::

    raspi-pir --help

License
-------

For more information see the `LICENSE <https://github.com/ricco386/RPi/blob/master/RPi.PIR/LICENSE>`_ file.
