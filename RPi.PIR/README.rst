RPi.PIR
#######

Python implementation for PIR sensor for Raspberry Pi.

Installation
------------

Make sure your system is able to compile Python extensions. On Raspbian or Debian/Ubuntu image you can ensure your system is ready by executing::

    sudo apt-get update
    sudo apt-get install build-essential python-dev

Install `RPi.Sensor <https://github.com/ricco386/RPi.Sensor>`_ library::

    sudo pip install --upgrade RPi.Sensor

Lastly install RPi.PIR app::

    pip install -e git+https://github.com/ricco386/RPi.git#egg=version_subpkg&subdirectory=RPi.PIR

**Dependencies:**

- `RPi.Sensor <https://github.com/ricco386/RPi.Sensor>`_ (0.3.0+)

License
-------

For more information see the `LICENSE <https://github.com/ricco386/RPi/blob/master/RPi.PIR/LICENSE>`_ file.
