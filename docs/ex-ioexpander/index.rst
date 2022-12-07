.. meta::
  :keywords: EX-CommandStation Command Station EX-IOExpander

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-CS-LOGO|

*************
EX-IOExpander
*************

|tinkerer|

.. note:: 

  |EX-IO| is currently in its infancy and as such is considered to be in Alpha testing, so could (and likely will) change without notice, and possibly even be broken in some scenarios.

|EX-IO| is an additional microcontroller utilised to expand the I/O port capability of an |EX-CS|, currently emulating the functionality of the MCP23017 I/O expander, and connecting to the |EX-CS| via |I2C|.

.. sidebar:: Credits

  |EX-IO| was inspired by the work of Mike B (@Springlake on Discord) and Ross (@Rosscoe on Discord) to emulate an MCP23017 device as part of a mimic panel design. The DCC-EX team have taken this inspiration, and now provided a generic MCP23017 emulation device.

Software requirements
=====================

There are currently no special requirements for the |EX-CS| version, and the |EX-IO| software can be found here:

.. rst-class:: dcclink

  `EX-IOExpander Github Repository <https://github.com/DCC-EX/EX-IOExpander>`_

Hardware requirements
=====================

|EX-IO| needs a dedicated, AVR based microcontroller (Arduino Uno or Nano at present) with up to 16 I/O pins available.

Using microcontrollers with less than 16 pins is possible, as the pins in use are configurable, however, microcontrollers with more than 16 pins will currently only be able to utilise up to 16 pins.

By implementing items such as the :ref:`ex-ioexpander/index:pin map` to disconnect the physical pin numbers from the virtual pins (VPins) used in the device driver, it is expected that this would be portable to other hardware platforms in due course.

Theory of operation
===================

In the current implementation, |EX-IO| simply replicates the functionality of an MCP23017, however it does not have interrupt capability enabled, so it must operate in polling mode only in the same manner as the default defined MCP23017 devices.

This means inputs and outputs can be defined, configured, and connected in the same manner as an MCP23017. Inputs can be utilised with or without pullups enabled.

Configuration
=============

Like |EX-CS|, |EX-TT|, and other |DCC-EX| products, configuration changes for |EX-IO| are made by editing "config.h". Again, like other products, an example "config.example.h" file is included that can be copied and edited to suit.

EX-CommandStation device driver
-------------------------------

To enable support for |EX-IO|, you need to enable this via "myHal.cpp" in your |EX-CS|. This simply utilises the existing "IO_MCP23017.h" device driver, so the only modification required is to add the entry to create the device:

.. code-block:: cpp

  MCP23017::create(800, 16, 0x90);

In this example, unused VPin 800 is used as the first VPin, with all 16 pins assigned, and using the default |I2C| address of 0x90.

Note that the number of pins defined here must match :ref:`ex-ioexpander/index:number_of_pins`.

I2C_ADDRESS
-----------

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Define I2C address
  //  Default 0x90, can be any valid, available I2C address
  // 
  #define I2C_ADDRESS 0x90

The default |I2C| address of 0x90 should be available, however this can be changed to any available address, and must match the device driver configuration in "myHal.cpp".

NUMBER_OF_PINS
--------------

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Define the number of I/O pins to use
  //  16 pins is the maximum here
  #define NUMBER_OF_PINS 16

The default is 16 pins, which is also the maximum. If using less, reduce this number to suit, noting it must match the number of pins specified in :ref:`ex-ioexpander/index:ex-commandstation device driver`, and you must specify the correct number of pins in :ref:`ex-ioexpander/index:pin map`.

If simply utilising an Uno or Nano as a direct MCP23017 replacement, you should not need to adjust this.

Pin map
-------

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Define the pin map
  //  Defining a pin map should allow portability to other platforms
  // 
  //  You must define the correct number of ports as per NUMBER_OF_PINS above
  //
  static uint8_t pinMap[NUMBER_OF_PINS] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, A0, A1, A2, A3};

This is used to map the physical microcontroller pins to the VPins defined by the device driver.

From left to right maps from the first to last VPin, so in our example in :ref:`ex-ioexpander/index:ex-commandstation device driver` starting with VPin 800, this will map to pin 2, with the last VPin 815 mapping to pin A3.

Note that this line contains a specific C++ syntax, and the only values that should be touched are the pin numbers themselves.

If simply utilising an Uno or Nano as a direct MCP23017 replacement, you should not need to adjust this.

DIAG
----

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Uncomment to enable diag output
  // 
  // #define DIAG

Uncommenting this line will enable extra diagnostic output to the serial console to help with diagnosis and troubleshooting in the event issues are encountered.

Looking for some help with EX-IOExpander?
===========================================

To raise a bug report, feature request, support request, or submit Beta test results, feel free to use our handy GitHub templates accessible by clicking this button:

|githublink-ex-ioexpander-button|