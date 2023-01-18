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

Arduino Mega2560
----------------

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
  * - SDA/SCL (20/21)
    - |I2C| connection for use with |I2C| displays, I/O expanders, etc.
  * - SDA/SCL (near USB)
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

----

Arduino Uno
-----------

.. raw:: html
  :file: ../../_static/images/pinouts/uno-pins.svg

.. list-table:: Uno Pins to avoid
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

.. list-table:: Mega2560 Pins to use
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Pin(s)
    - Details
  * - SDA/SCL (A4/A5)
    - |I2C| connection for use with |I2C| displays, I/O expanders, etc.
  * - SDA/SCL (near USB)
    - |I2C| connection for use with |I2C| displays, I/O expanders, etc.
  * - 2
    - Digital I/O pin available for use

.. list-table:: Mega2560 Pins to use with caution
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Pin(s)
    - Details
  * - A2 - A3
    - Analogue I/O pins available by default, but may be in use for additional current sensing
  * - Tx0/Rx0
    - Can be used for WiFi or Bluetooth adapters but coexists with onboard USB and will need to be disconnected for software uploads
  * - 5 - 9
    - Digital I/O pins available by default, but some motor shields or other peripherals use these

----

I/O expanders
=============

.. note:: 

  If using an |I2C| LCD display with the PCF8574 backpack, it is possible that it resides at |I2C| address 0x27. If this is the case, you need to either not use any other devices at this address, change the PCF8574 address to 0x3F (if possible), or replace it. OLEDs typically use address 0x3C, so should not cause issues.

  Refer to :doc:`/reference/hardware/i2c-displays` for further information.

MCP23017 digital I/O expander
-----------------------------

MCP23017 I/O expanders have 16 digital I/O pins and 8 available |I2C| addresses from 0x20 to 0x27.

The device driver name is "IO_MCP23017.h", however this is included by default and does not need to be added to "myHal.cpp".

Two devices are defined by default.

Refer to :ref:`reference/developers/hal-config:mcp23017 modules` and :ref:`reference/developers/hal:hal programming interface` for further information.

.. list-table:: Default defined MCP23017s
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - |I2C| address
    - VPin range
    - Comments
  * - 0x20
    - 164 - 179
    - | Defined by default, default |I2C| address on some breakout boards
      | Some breakout boards (eg. Waveshare) have 0x27 as default and will need to be changed
  * - 0x21
    - 180 - 195
    - Defined by default, address typically needs to be configured on breakout boards

When adding more MCP23017s, select an unused VPin that allows a total of 16 consecutive numbers for all I/O pins.

.. list-table:: Additional MCP23017s

  * - |I2C| address range
    - VPin count
    - Comments
  * - 0x22 - 0x27
    - 16
    - Need to add to myHal.cpp, and |I2C| address typically needs to be configured on breakout boards

----

MCP23008 digital I/O expander
-----------------------------

MCP23008 I/O expanders have 8 digital I/O pins and 8 available |I2C| addresses from 0x20 to 0x27.

The device driver name is "IO_MCP23008.h" and will need to be included in "myHal.cpp".

Note that devices at 0x20/0x21 will conflict with the default defined MCP23017 devices at these addresses, and you will need to edit "IODevice.cpp" in order to disable these.

Refer to :ref:`reference/developers/hal:hal programming interface` for further information.

When adding MCP23008s, select an unused VPin that allows a total of 8 consecutive numbers for all I/O pins.

.. list-table:: Adding MCP23008s

  * - |I2C| address range
    - VPin count
    - Comments
  * - 0x20 - 0x27
    - 8
    - | Need to add to myHal.cpp, and |I2C| address typically needs to be configured on breakout boards
      | May need to disable default MCP23017s if 0x20/0x21 are used

----

PCF8574 digital I/O expander
----------------------------

PCF8574 I/O expanders have 8 digital I/O pins and 8 available |I2C| addresses from 0x20 to 0x27.

The device driver name is "IO_PCF8574.h" and will need to be included in "myHal.cpp".

Note that devices at 0x20/0x21 will conflict with the default defined MCP23017 devices at these addresses, and you will need to edit "IODevice.cpp" in order to disable these.

Refer to :ref:`reference/developers/hal:hal programming interface` for further information.

When adding PCF8574s, select an unused VPin that allows a total of 8 consecutive numbers for all I/O pins.

.. list-table:: Adding PCF8574s

  * - |I2C| address range
    - VPin count
    - Comments
  * - 0x20 - 0x27
    - 8
    - | Need to add to myHal.cpp, and |I2C| address typically needs to be configured on breakout boards
      | May need to disable default MCP23017s if 0x20/0x21 are used

----

PCA9685 PWM servo module
------------------------

PCA9685 servo modules (or I/O expanders) have 16 PWM output pins and 62 available |I2C| addresses from 0x40 to 0x7D.

The device driver name is "IO_PCA9685.cpp", however this is loaded by default and does not need to be added to "myHal.cpp".

Two devices are defined by default.

Refer to :ref:`reference/developers/hal-config:pca9685 modules` and :ref:`reference/developers/hal:hal programming interface` for further information.

.. list-table:: Default defined PCA9685s
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - |I2C| address
    - VPin range
    - Comments
  * - 0x40
    - 100 - 115
    - Defined by default, typically default |I2C| address on breakout boards
  * - 0x41
    - 116 - 131
    - Defined by default, address typically needs to be configured on breakout boards

When adding more PCA9685s, select an unused VPin that allows a total of 16 consecutive numbers for all I/O pins.

.. list-table:: Additional PCA9685s

  * - |I2C| address range
    - VPin count
    - Comments
  * - 0x42 - 0x7D
    - 16
    - Need to add to myHal.cpp, and |I2C| address typically needs to be configured on breakout boards

----

EX-IOExpander - digital and analogue I/O expander
-------------------------------------------------

EX-IOExpander is designed to support up to 256 pins and is currently in testing. The default |I2C| address is 0x65, however any valid and available address can be used.

The device driver name is "IO_EXIOExpander.h" and will need to be included in "myHal.cpp".

Refer to :doc:`/ex-ioexpander/index` for further information.

When adding EX-IOExpander devices, select an unused VPin that allows for the appropriate number of consecutive vpins for all I/O pins.

.. list-table:: Additional MCP23017s

  * - |I2C| address range
    - VPin count
    - Comments
  * - Any valid/available (default 0x65)
    - 16 - 256
    - Need to add to myHal.cpp, and |I2C| address needs to be configured in software

----

Sensors
=======

VL53L0X time-of-flight sensor
-----------------------------

VL53L0X time-of-flight sensors have a default |I2C| address of 0x29, however this address is programmable by software.

The device driver name is "IO_VL53L0X.h" and will need to be included in "myHal.cpp".

Refer to :doc:`/ex-commandstation/accessories/sensors/vl53l0x-tof-sensor` for further information.

.. list-table:: Adding VL53L0Xs

  * - |I2C| address range
    - Suggested first VPin
    - VPin count
    - Comments
  * - 0x29 - 0x7F
    - 4000
    - 3
    - Need to add to myHal.cpp, do not use |I2C| address 0x29 if using multiple devices

----

Other devices
=================

EX-Turntable
------------

.. note:: 

  |EX-TT| is in Beta testing, however the device driver is unlikely to change much if at all.

|EX-TT| is configured with a default |I2C| address of 0x60, however this address is configurable by the software.

The device driver name is "IO_EXTurntable.h" and will need to be included in "myHal.cpp".

Refer to :doc:`/ex-turntable/index` for further information.

.. list-table:: Adding EX-Turntable

  * - |I2C| address and range
    - Suggested VPin
    - VPin count
    - Comments
  * - 0x60 default, any valid and available |I2C| address
    - 600
    - 1
    - Need to add to myHal.cpp, and use the specified version of |EX-CS|

----

DCC-EX rotary encoder
---------------------

|NOT-IN-PROD-VERSION|

.. note:: 

  The rotary encoder device driver is in early development and is likely to change.

The DCC-EX rotary encoder is configured with a default |I2C| address of 0x80, however this address is configurable by the software.

The device driver name is "IO_RotaryEncoder.h" and will need to be included in "myHal.cpp".

Refer to :ref:`ex-turntable/test-and-tune:controlling ex-turntable with a rotary encoder` and the `project page <https://petegsx-projects.github.io/rotary-encoder/index.html>`_ for further information.

.. list-table:: Adding DCC-EX rotary encoder

  * - |I2C| address and range
    - Suggested VPin
    - VPin count
    - Comments
  * - 0x80 default, any valid and available |I2C| address
    - 800
    - 1
    - Need to add to myHal.cpp, and use the specified version of |EX-CS|