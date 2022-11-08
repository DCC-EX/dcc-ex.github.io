.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-REF-LOGO|

************************************************
Default Pin/VPin Allocations and Recommendations
************************************************

|conductor| |tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

On this page, we aim to outline and summarise the various default and recommended pins (and vpins for I/O expanders) for use with various input and output devices for our primary suported microcontrollers and I/O devices and expanders. We will also include the default |I2C| addresses where appropriate.

Microcontrollers
================

This section outlines pins to avoid, pins that are free to use, and pins that are to be used with caution for each of our primary supported microcontrollers. The pins are grouped as such:

.. image:: /_static/images/pinouts/pin-legend.png
  :alt: Pinout legend
  :scale: 100%

Mega2560
--------

.. raw:: html
  :file: ../../_static/images/pinouts/mega2560-pins.svg

.. list-table:: Mega2560 Pins to avoid
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Pin(s)
    - Details
  * - A0 - A1
    - Analogue I/O pins used for main and program track current sensing
  * - 3 - 4
    - Digital I/O pins commonly used by motor shields or Ethernet shields
  * - 10 - 13
    - Digial I/O pins commonly used by motor shields
  * - 50 - 53
    - Digital I/O pins reserved for special system utilities


.. list-table:: Mega2560 Pins to use
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Pin(s)
    - Details
  * - SDA/SCL
    - |I2C| connection for use with |I2C| displays, I/O expanders, etc.
  * - Tx1/Rx1/Tx2/Rx2/Tx3/Rx3
    - Additional serial ports available for use
  * - A8 - A15
    - Analogue I/O pins available for use
  * - 2
    - Digital I/O pin available for use
  * - 22 - 49
    - Digital I/O pins available for use

.. list-table:: Mega2560 Pins to use with caution
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Pin(s)
    - Details
  * - A2 - A7
    - Analogue I/O pins available by default, but may be in use for additional current sensing
  * - Tx0/Rx0
    - Can be used for WiFi or Bluetooth adapters but coexists with onboard USB and will need to be disconnected for software uploads
  * - 5 - 9
    - Digital I/O pins available by default, but some motor shields or other peripherals use these

-

Uno
---

.. raw:: html
  :file: ../../_static/images/pinouts/uno-pins.svg

.. list-table:: Uno Pins to avoid
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Pin(s)
    - Description
  * - 1
    - A pin

.. list-table:: Uno Pins to use
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Pin(s)
    - Description
  * - 1
    - A pin

.. list-table:: Uno Pins to use with caution
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Pin(s)
    - Description
  * - 1
    - A pin

I/O expanders
=============

MCP23017
--------

0x

MCP23008
--------



PCA9685
-------



Sensors
=======

VL53L0X
-------

0x29

Other
=====

EX-Turntable
------------

0x60
600

DCC-EX rotary encoder
---------------------

|NOT-IN-PROD-VERSION|

0x80
700