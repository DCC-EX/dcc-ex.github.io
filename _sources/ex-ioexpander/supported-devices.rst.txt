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
  * - Digital pins
    - 12
    - 16
  * - Analogue pins
    - 2
    - 6

.. note:: 

  On Arduino Nano, the additional analogue pins A6/7 are analogue only can cannot be used as digital inputs or outputs.

.. csv-table:: Arduino Nano and Pro Mini EX-IOExpander pin map at Vpin 800
  :widths: auto
  :stub-columns: 1

  Vpins,800,801,802,803,804,805
  Digital Pins,D2,D3,D4,D5,D6,D7
  Vpins,806,807,808,809,810,811
  Digital Pins,D8,D9,D10,D11,D12,D13
  Vpins,812,813,814,815,816,817
  Analogue Pins,A0,A1,A2,A3,A6,A7

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
  * - Digital pins
    - 12
    - 16
  * - Analogue pins
    - 0
    - 4

.. csv-table:: Arduino Uno EX-IOExpander pin map at Vpin 800
  :widths: auto
  :stub-columns: 1

  Vpins,800,801,802,803,804,805
  Digital Pins,D2,D3,D4,D5,D6,D7
  Vpins,806,807,808,809,810,811
  Digital Pins,D8,D9,D10,D11,D12,D13
  Vpins,812,813,814,815
  Analogue Pins,A0,A1,A2,A3

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

.. note:: 

  PC13 has a switch (blue button) with pullup resistor attached, so this is suitable as an input only (without pullups enabled) unless you disconnect SB17.

  In addition, PA5 is the green LED.

.. list-table:: NUCLEO-F411RE pin allocations
  :widths: auto
  :header-rows: 1
  :stub-columns: 1
  :class: command-table

  * - Total pins 40
    - Minimum
    - Maximum
  * - Digital pins
    - 26
    - 40
  * - Analogue pins
    - 0
    - 14

.. csv-table:: F411RE EX-IOExpander pin map at Vpin 800
  :widths: auto
  :stub-columns: 1

  Vpins,800,801,802,803,804,805,806
  CN7 Digital Pins,PC10,PC11,PC12,PD2,PA15,PB7,PC13
  Vpins,807,808,809,810,811,812,813,814,815,816
  CN10 Digital Pins,PC9,PC8,PC6,PA12,PA11,PB12,PB6,PC7,PA9,PB2
  Vpins,817,818,819,820,821,822,823,824,825
  CN10 Digital Pins,PA8,PB10,PB15,PB4,PB14,PB5,PB13,PB3,PA10
  Vpins,826,827,828,829,830,831,832,833
  CN7 Analogue Pins,PA0,PA1,PA4,PB0,PC2,PC1,PC3,PC0
  Vpins,834,835,836,837,838,839
  CN10 Analogue Pins,PC5,PA5,PA6,PA7,PB1,PC4

|

STMicroelectronics NUCLEO-F412ZG
================================

.. warning:: 

  Support for the F412ZG is experimental at best right now. While the software compiles and it appears to operate normally, no actual I/O testing has been performed.

The Nucleo F412ZG is a 3v3 microcontroller with significantly more available I/O pins than an Arduino Mega. The pin numbers used are defined using the Morpho pin names, in ascending order of the pin number for each Morpho connector, hence the pin names aren't sequential.

Numerous I/O pins are connected to other devices or perform multiple functions which result in pin conflicts, so the only pins included are those that are able to successfully be set to input mode on startup.

.. note:: 

  PC13 has a switch (blue button) with pullup resistor attached, so this is suitable as an input only (without pullups enabled) unless you disconnect SB17.

  In addition, PB0 is the green LED, PB7 is the blue LED, and PB14 in the red LED.

.. list-table:: NUCLEO-F412ZG pin allocations
  :widths: auto
  :header-rows: 1
  :stub-columns: 1
  :class: command-table

  * - Total pins 98
    - Minimum
    - Maximum
  * - Digital pins
    - 82
    - 98
  * - Analogue pins
    - 0
    - 16

.. csv-table:: F412ZG EX-IOExpander pin map at Vpin 800
  :widths: auto
  :stub-columns: 1

  Vpins,800,801,802,803,804,805,806,807,808,809
  CN11 Digital Pins,PC10,PC11,PC12,PD2,PF6,PF7,PA15,PB7,PC13,PD4
  Vpins,810,811,812,813,814,815,816,817,818,819
  CN11 Digital Pins,PD3,PD5,PG2,PD6,PG3,PD7,PE2,PE3,PE4,PE5
  Vpins,820,821,822,823,824,825,826,827,828,829
  CN11 Digital Pins,PF1,PF2,PF0,PF8,PD1,PF9,PD0,PG1,PG0,PE1
  Vpins,830,831,832,833,834,835,836,837
  CN11 Digital Pins,PE6,PG9,PG15,PG12,PG10,PH_2,PG13,PG11
  Vpins,838,839,840,841,842,843,844,845,846,847
  CN12 Digital Pins,PC9,PC8,PC6,PB12,PB6,PB11,PC7,PB2,PB10,PB15
  Vpins,848,849,850,851,852,853,854,855,856,857
  CN12 Digital Pins,PB4,PB14,PB5,PB13,PB3,PF5,PF4,PE8,PD13,PF10
  Vpins,858,859,860,861,862,863,864,865,866,867
  CN12 Digital Pins,PD12,PE7,PD11,PD14,PE10,PD15,PE12,PF14,PE14,PE9
  Vpins,868,869,870,871,872,873,874,875,876,877
  CN12 Digital Pins,PE15,PE13,PE11,PF13,PF3,PF12,PF15,PG14,PF11,PE0
  Vpins,878,879,880,881
  CN12 Digital Pins,PD10,PG8,PG5,PG4
  Vpins,882,883,884,885,886,887,888,889
  CN11 Analogue Pins,PA0,PA1,PA4,PB0,PC2,PC1,PC3,PC0
  Vpins,890,891,892,893,894,895,896,897
  CN12 Analogue Pins,PC5,PA5,PA6,PA7,PB1,PC4,PA2,PA3

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