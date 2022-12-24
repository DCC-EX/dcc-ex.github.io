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

  When configuring the device driver, all available pins must be accounted for as either digital or analogue pins, even if there is no intended use.

Arduino Nano
============

.. image:: /_static/images/ex-ioexpander/ex-ioexpander-nano.png
  :alt: EX-IOExpander on Arduino Nano
  :scale: 5%

Device driver macros available:

- EXIO_NANO_DIGITAL_PINS - 12
- EXIO_NANO_ANALOGUE_PINS - 6

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

Device driver macros available:

- EXIO_UNO_DIGITAL_PINS - 12
- EXIO_UNO_ANALOGUE_PINS - 4

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

Device driver macros available:

- EXIO_MEGA_DIGITAL_PINS - 46
- EXIO_MEGA_ANALOGUE_PINS - 16

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
  
.. STMicroelectronics NUCLEO-F411RE
.. ================================

.. Device driver macros available:

.. - EXIO_F411RE_DIGITAL_PINS - 46
.. - EXIO_F411RE_ANALOGUE_PINS - 16

.. .. list-table:: NUCLEO-F411RE pin allocations
..   :widths: auto
..   :header-rows: 1
..   :stub-columns: 1
..   :class: command-table

..   * - Total pins 62
..     - Minimum
..     - Maximum
..     - Notes
..   * - Digital pins
..     - 46
..     - 62
..     - D2 - D19, D22 - D49, A0 - A15, noting D20/D21 and D50 - D53 are reserved
..   * - Analogue pins
..     - 0
..     - 16
..     - A0 - A15