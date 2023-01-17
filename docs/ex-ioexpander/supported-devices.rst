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

|

Arduino Pro Mini
================

The Arduino Pro Mini comes in two variations; a 3.3V running at 8MHz, and a 5V running at 16MHz.

.. warning:: 

  The 8MHz 3.3V Pro Mini is not 5V tolerant

The Pro Mini uses an identical pin map to the :ref:`ex-ioexpander/supported-devices:arduino nano`.

|

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

|

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

|

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

|

Adding new devices
==================

|tinkerer| |engineer|

.. warning:: 

  When considering adding new devices to |EX-IO|, be sure to take into account whether they are 5V or 3.3V devices, and whether their I/O and |I2C| pins are 5V tolerant if they are 3.3V devices. New generation microcontrollers tend to be 3.3V, and some have 5V tolerant I/O pins (eg. STM32 Nucleo), but some are not 5V tolerant (eg. SAMD).

  To connect 3.3V devices to a 5V |EX-CS|, they need to either be 5V tolerant, or you will need to use a level shifter to avoid letting the magic smoke out.

Adding new devices to the |EX-IO| software is fairly straight forward, and only requires additional information in the |EX-IO| software itself, with no changes required to the device driver loaded in your |EX-CS|.

In order to successfully add an additional device, you need to know the C++ preprocessor macro definitions for the architecture or platform, and for the specific variant or board itself. In addition, you need to specify how the Vpins defined in the device driver map to the physical pins of the |EX-IO| device.

For example, the AVR series (Uno, Mega, Nano) have the architure or platform macro defined as "ARDUINO_ARCH_AVR", with the Nano having the variant or board specific macro "ARDUINO_AVR_NANO", and there is a pin map defined that maps to this macro definition.

Enabling software reboots
-------------------------

The architecture or platform macro is used to determine the correct method to reboot the device via the ``<Z>`` command, whereas the variant or board specific macro is used to define the actual pins in use.

If a new architecture or platform is being added, then "EX-IOExpander.ino" will need to be updated with the suitable software command in the "reset()" function, otherwise a reboot via ``<Z>`` will not be available.

If the architecture or platform already exists, or there is no desire to reboot via software, then the only change required is to add the variant or board specific information to "SupportedDevices.h".

Defining the device and pin map in SupportedDevices.h
-----------------------------------------------------

A pin map is used to map the Vpins from the device driver in the |EX-CS| to the appropriate physical pins on the |EX-IO| device, and therefore defining this in the correct order in the |EX-IO| software is critical. It is equally critical to ensure that the correct variant or board macro is used to ensure the correct pin map is used when compiling and uploading the software to the |EX-IO| device.

Pin maps are defined in the file "SupportedDevices.h".

As per :ref:`ex-ioexpander/overview:pin/vpin allocation`, digital pins are allocated first, incrementing from the first Vpin, and analogue pins are allocated in reverse, starting from the last Vpin.

These are the considerations when defining the pin map:

- All pins capable of being digital inputs/outputs need to be included in "digitalPinMap", including analogue capable pins
- All pins capable of being analogue inputs need to be included in "analoguePinMap" (don't include dual digital/analogue pins here)
- Pins included in both pin maps need to be in the same order, with analogue pins at the end of the digital pin map
- Macros for the number of pins in each pin map must be defined accurately
- NUMBER_OF_DIGITAL_PINS is the number of digital only pins
- NUMBER_OF_ANALOGUE_PINS is the number of pins capable of analogue input, whether or not they can be used as digital also
- Any pins that are only capable of analogue inputs must be at the end of the analogue pin map

Further to this, if EEPROM is available, this needs to be defined, along with a description that is presented in the serial console when starting the device.

To use the Arduino Nano as the example, this is the definition in "SupportedDevices.h":

.. code-block:: cpp

  // Arduino Nano
  #elif defined(ARDUINO_AVR_NANO)
  #define BOARD_TYPE F("Nano")
  #define HAS_EEPROM
  #define NUMBER_OF_DIGITAL_PINS 12   // D2 - D13
  #define NUMBER_OF_ANALOGUE_PINS 6     // A0 - A3, A6/A7, cannot use A4/A5
  static const uint8_t digitalPinMap[NUMBER_OF_DIGITAL_PINS + NUMBER_OF_ANALOGUE_PINS] = {
    2,3,4,5,6,7,8,9,10,11,12,13,A0,A1,A2,A3
  };
  static const uint8_t analoguePinMap[NUMBER_OF_ANALOGUE_PINS] = {
    A0,A1,A2,A3,A6,A7
  };

- The variant or board macro definition is "ARDUINO_AVR_NANO".
- The "BOARD_TYPE" is displayed in the serial console at startup as "Nano".
- The Nano has EEPROM support to allow storing the |I2C| address
- There are 12 digital pins
- There are 6 analogue pins
- All digital pins and the 4 analogue pins capable of digital are defined in "digitalPinMap"
- All analogue pins are defined in "analoguePinMap"
- The analogue pins defined in both pin maps are added in the same order, with analogue pins at the end of the digital pin map
- Analogue pins A6/A7 are analogue only, are therefore not included in digitalPinMap, and are defined at the end of analoguePinMap