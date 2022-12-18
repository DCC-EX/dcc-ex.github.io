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

|NOT-IN-PROD-VERSION|

|EX-IO| is an additional microcontroller utilised to expand the I/O port capability of an |EX-CS| and connecting via |I2C|.

|EX-IO| can utilise digital input and output pins as well as analogue input pins, depending on the chosen microcontroller.

.. sidebar:: Credits

  |EX-IO| was inspired by the work of Mike B (@Springlake on Discord) and Ross (@Rosscoe on Discord) to emulate an MCP23017 device as part of a mimic panel design. The DCC-EX team have taken this inspiration, and now provided a generic MCP23017 emulation device.

Software requirements
=====================

To utilise |EX-IO|, you must be running the "add-ex-ioexpander" branch of |EX-CS| which is available here:

.. rst-class:: dcclink

  `EX-CommandStation with EX-IOExpander device driver <https://github.com/DCC-EX/CommandStation-EX/tree/add-ex-ioexpander>`_


In addition, you will require the |EX-IO| software which can be found here:

.. rst-class:: dcclink

  `EX-IOExpander Github Repository <https://github.com/DCC-EX/EX-IOExpander>`_

Hardware requirements
=====================

|EX-IO| needs a dedicated microcontroller connected to the |I2C| bus of your |EX-CS|.

In the current implementation, the only supported microcontrollers are Arduino Uno, Nano, and Mega. The device driver and |EX-IO| software are being written in such a way that should enable porting to other microcontroller architectures, and is expected to support up to 256 I/O pins.

Theory of operation
===================

In the current implementation, |EX-IO| can utilise digital pins in both input and output mode, and analogue pins in input mode. Digital pins in input mode can have pullups enabled or disabled.

Pins capable of both digital and analogue can be used for either purpose.

Configuration
=============

Aside from configuring the |I2C| address of your |EX-IO| device, the device driver loaded in your |EX-CS| will perform the necessary run time configuration at startup, meaning you should only ever need to update the |EX-IO| software when a new version is available.

Configuration changes for |EX-IO| are made by editing a "myConfig.h" file. An example "myConfig.example.h" file is included that can be copied and edited to suit. The only configuration item you should really need to consider is :ref:`ex-ioexpander/index:i2c_address`.

EX-CommandStation device driver
-------------------------------

To enable support for |EX-IO|, you need to enable this via "myHal.cpp" in your |EX-CS|. You will need to load the |EX-IO| device driver in addition to creating the device(s).

To create the |EX-IO| device, the syntax is `EXIOExpander::create(vpin, npins, address, digital_pins, analogue_pins);` where:

- vpin = An unused vpin
- npins = Total number of vpins to assign to the device (must equal digital_pins + analogue_pins)
- address = An available |I2C| address (default 0x65)
- digital_pins = The number of digital pins to enable
- analogue_pins = The number of analogue pins to enable

To use default configurations for the various supported platforms, macros have been defined to utilise all available digital and analogue pins for these platforms:

- EXIO_UNO_DIGITAL_PINS - D2 - D13 on Uno
- EXIO_UNO_ANALOGUE_PINS - A0 - A3 on Uno
- EXIO_NANO_DIGITAL_PINS - D2 - D13 on Nano
- EXIO_NANO_ANALOGUE_PINS - A0 - A3, A6/A7 on Nano
- EXIO_MEGA_DIGITAL_PINS - D2 - D19, D22 - D49 on Mega
- EXIO_MEGA_ANALOGUE_PINS - A0 - A15 on Mega

In the example below, we will configure an Arduino Nano using the default pin counts at address 0x65, with an additional device using all available digital capable pins and no analogue pins at address 0x66.

.. code-block:: cpp

  #include "IO_EXIOExpander.h"

  void halSetup() {
    ...
    EXIOExpander::create(800, 18, 0x65, EXIO_NANO_DIGITAL_PINS, EXIO_NANO_ANALOGUE_PINS);
    EXIOExpander::create(820, 16, 0x66, 16, 0);
  }

I2C_ADDRESS
-----------

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Define I2C address
  //  Default 0x65, can be any valid, available I2C address
  // 
  #define I2C_ADDRESS 0x65

The default |I2C| address of 0x65 should be available, however this can be changed to any available address, and must match the device driver configuration in "myHal.cpp".

DIAG
----

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Uncomment to enable diag output
  // 
  // #define DIAG

Uncommenting this line will enable extra diagnostic output to the serial console to help with diagnosis and troubleshooting in the event issues are encountered.

DIAG_CONFIG_DELAY
-----------------

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Delay between dumping the status of the port config if DIAG enabled
  // 
  #define DIAG_CONFIG_DELAY 3000

When :ref:`ex-ioexpander/index:diag` is enabled, the configuration of each pin is displayed continuously to be able to monitor the configuration and state of each pin. By default, this will display every 3 seconds (3000ms). This configuration item allows the delay between updates to be increased or decreased.

Looking for some help with EX-IOExpander?
===========================================

To raise a bug report, feature request, support request, or submit Beta test results, feel free to use our handy GitHub templates accessible by clicking this button:

|githublink-ex-ioexpander-button|