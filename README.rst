RPi.DHT
#######

Python implementation for Adafruit_DHT sensor for Raspberry Pi.

To connect to Raspberry Pi plug into GPIO PIN 21 and GROUD and POWER PIN. Install and execute RPi.DHT and it should work. Alternatively you can user different PIN and execute doorman with parameter: ``rpi-dht --pin pin_number``.


.. image:: doc/RPi.DHT.png


Installation
------------

RPi.DHT needs `Adafruit Python DHT Sensor Library <https://github.com/adafruit/Adafruit_Python_DHT>`_. Make sure your system is able to compile Python extensions.On Raspbian or Debian/Ubuntu image you can ensure your system is ready by executing::

    sudo apt-get update
    sudo apt-get install build-essential python-dev

Install the library by downloading with the download link on the right, unzipping the archive, and executing::

    pip install https://github.com/adafruit/Adafruit_Python_DHT/tarball/master

Install `RPi.Sensor <https://github.com/ricco386/RPi.Sensor>`_ library::

    pip install https://github.com/ricco386/RPi.Sensor/tarball/master

Lastly install RPi.DHT appi::

    pip install https://github.com/ricco386/RPi.DHT/tarball/master

**Dependencies:**

- `Adafruit_DHT <https://github.com/adafruit/Adafruit_Python_DHT>`_
- `RPi.Sensor <https://github.com/ricco386/RPi.Sensor>`_ (0.1.0+)

License
-------

For more information see the `LICENSE <https://github.com/ricco386/RPi.DHT/blob/master/LICENSE>`_ file.
