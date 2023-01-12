.. meta::
  :keywords: EX-CommandStation Command Station EX-IOExpander

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-IO-LOGO|

*****************
Supported Devices
*****************

|tinkerer| |githublink-ex-ioexpander-button2|

.. sidebar:: 
  
  .. contents:: On this page
    :depth: 2
    :local:

This page outlines the microcontrollers that are supported for use with |EX-IO|, including outlining the pins available for use.

When uploading the |EX-IO| software, the device type is detected by the compiler in either the Arduino IDE or PlatformIO, so no configuration is necessary on the |EX-IO| device itself (aside from the |I2C| address of course).

All allocation of pins is done via the device driver (see :ref:`ex-ioexpander/overview:ex-commandstation device driver`).

.. note:: 

  When configuring the device driver, all available pins must be accounted for as either digital or analogue pins, even if there is no intended use for every individual pin.

Arduino Nano
============

.. image:: /_static/images/ex-ioexpander/ex-ioexpander-nano.png
  :alt: EX-IOExpander on Arduino Nano
  :scale: 5%

.. list-table:: Arduino Nano pin allocations
  :widths: auto
  :header-rows: 1
  :stub-columns: 1
  :class: command-table

  * - Total pins 18
    - Minimum
    - Maximum
    - Notes
  * - Digital pins
    - 12
    - 16
    - D2 - D13, A0 - A3
  * - Analogue pins
    - 2
    - 6
    - A0 - A3, A6 - A7, note A4/A5 are |I2C|, and A6/A7 analogue only

Arduino Uno
===========

.. image:: /_static/images/ex-ioexpander/ex-ioexpander-uno.png
  :alt: EX-IOExpander on Arduino Uno
  :scale: 5%

.. list-table:: Arduino Uno pin allocations
  :widths: auto
  :header-rows: 1
  :stub-columns: 1
  :class: command-table

  * - Total pins 16
    - Minimum
    - Maximum
    - Notes
  * - Digital pins
    - 12
    - 16
    - D2 - D13, A0 - A3
  * - Analogue pins
    - 0
    - 4
    - A0 - A3, note A4/A5 are |I2C|

Arduino Mega2560
================

.. image:: /_static/images/ex-ioexpander/ex-ioexpander-mega.png
  :alt: EX-IOExpander on Arduino Mega2560
  :scale: 5%

.. list-table:: Arduino Mega pin allocations
  :widths: auto
  :header-rows: 1
  :stub-columns: 1
  :class: command-table

  * - Total pins 62
    - Minimum
    - Maximum
    - Notes
  * - Digital pins
    - 46
    - 62
    - D2 - D19, D22 - D49, A0 - A15, noting D20/D21 and D50 - D53 are reserved
  * - Analogue pins
    - 0
    - 16
    - A0 - A15
  
STMicroelectronics NUCLEO-F411RE
================================

.. warning:: 

  Support for the F411RE is experimental at best right now. While the software compiles and it appears to operate normally, no actual I/O testing has been performed.

.. image:: /_static/images/nucleo/nucleo-f411re-pinout.png
  :alt: Nucleo F411RE pin out
  :scale: 60%

The Nucleo F411RE is a 3v3 microcontroller with more available I/O pins than an Arduino Uno. The pin numbers used are defined using the Morpho pin names, in ascending order of the pin number for each Morpho connector, hence the pin names aren't sequential.

Numerous I/O pins are connected to other devices or perform multiple functions which result in pin conflicts, so the only pins included are those that are able to successfully be set to input mode on startup.

.. list-table:: NUCLEO-F411RE pin allocations
  :widths: auto
  :header-rows: 1
  :stub-columns: 1
  :class: command-table

  * - Total pins 37
    - Minimum
    - Maximum
    - Notes
  * - Digital pins
    - 25
    - 37
    - | PC_10,PC_11,PC_12,PD_2,PC_13,PC_14,PC_15,PH_0,PH_1 - CN7
      | PC_9,PC_8,PC_6,PA_12,PA_11,PB_12,PC_7,PA_9,PB_2,PA_8,PB_10,PB_15,PB_14,PB_5,PB_13,PA_10 - CN10
  * - Analogue pins
    - 0
    - 12
    - | PA_4,PB_0,PC_2,PC_1,PC_3,PC_0 - CN7
      | PC_5,PA_5,PA_6,PA_7,PB_1,PC_4 - CN10

Adding new devices
==================

You need to know:

- Platform/architecture/processor specific define for the preprocessor eg. "ARDUINO_ARCH_AVR" for reset functionality ``<Z>``
- Board specific define for the pin map eg. "ARDUINO_NUCLEO_F412ZG"
- If it's not in use already, requires an addition to the reset() function in EX-IOExpander.ino, otherwise no ``<Z>``

Pin map:

- Pin maps defined in SupportedDevices.h
- All pins capable of being digital inputs/outputs need to be included in "digitalPinMap", including analogue capable pins
- All pins capable of being analogue inputs need to be included in "analoguePinMap"
- The pin maps must be ordered in the same way, meaning pins in both pin maps need to be at the end of digital, beginning of analogue
- Macros must be defined accurately for digital and analogue pin maps