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

This section outlines pins to avoid, pins that are free to use, and pins that are to be used with caution for each of our primary supported microcontrollers.

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
    - Analogue I/O pins used for current sensing
  * - 3 - 4
    - Digital I/O pins commonly used by...
  * - 10 - 13
    - Digial I/O pins commonly used by...
  * - 50 - 53
    - Digital I/O pins reserved for...


.. list-table:: Mega2560 Pins to use
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Pin(s)
    - Details
  * - 1
    - A pin

.. list-table:: Mega2560 Pins to use with caution
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Pin(s)
    - Details
  * - 1
    - A pin

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