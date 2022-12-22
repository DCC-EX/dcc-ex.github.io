.. meta::
  :keywords: EX-CommandStation Command Station EX-IOExpander

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-IO-LOGO|

********
Overview
********

|tinkerer| |githublink-ex-ioexpander-button2|

.. note:: 

  |EX-IO| is currently in its infancy and as such is considered to be in Alpha testing, so could (and likely will) change without notice, and possibly even be broken in some scenarios.

|NOT-IN-PROD-VERSION|

.. sidebar:: 
  
  .. contents:: On this page
    :depth: 2
    :local:

Introduction
============

|EX-IO| is an additional microcontroller utilised to expand the I/O port capability of an |EX-CS| and connecting via |I2C|.

|EX-IO| can utilise digital input and output pins as well as analogue input pins, depending on the chosen microcontroller.

Rather than emulate any specific type of existing I/O expander, |EX-IO| has been written to integrate directly with |EX-CS| via its own device driver, which is how both digital and analogue pins can easily be utilised on the same device.

This page provides the general overview of |EX-IO|, as well as outlining the configuration options available.

.. note:: Credits

  |EX-IO| was inspired by the work of Mike B (@Springlake on Discord) and Ross (@Rosscoe on Discord) to emulate an MCP23017 device as part of a mimic panel design. The DCC-EX team have taken this inspiration and now provide a generic Arduino based I/O expander, able to utilise both digital and analogue pins.

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

Refer to :doc:`/ex-ioexpander/supported-devices` for the specific list, including which pins are available for use.

Theory of operation
===================

In the current implementation, |EX-IO| can utilise digital pins in both input and output mode, and analogue pins in input mode. Digital pins in input mode can have pullups enabled or disabled.

Pins capable of both digital and analogue can be used for either purpose.

As per other I/O devices, |EX-IO| can function with both the ``<S ...>`` sensor/input and ``<Z ...>`` output |DCC-EX| commands, as well as the various ``AT(), IF(), ATGTE(), IFGTE()`` type |EX-R| commands.

Configuration
=============

Aside from configuring the |I2C| address of your |EX-IO| device, the device driver loaded in your |EX-CS| will perform the necessary run time configuration at startup, meaning you should only ever need to update the |EX-IO| software when a new version is available.

Configuration changes for |EX-IO| are made by editing a "myConfig.h" file. An example "myConfig.example.h" file is included that can be copied and edited to suit. The only configuration item you should really need to consider is :ref:`ex-ioexpander/overview:i2c_address`.

Pin/Vpin allocation
-------------------

All available pins on the chosen |EX-IO| device must be allocated as either digital or analogue pins. Details of the pins available for use are outlined on the :doc:`/ex-ioexpander/supported-devices` page.

Vpins are allocated by the |EX-CS| device driver, with digital pins allocated by incrementing from the first Vpin, and analogue pins decrementing from the highest allocated Vpin number.

For example, an Arduino Nano has a total of 22 I/O pins (D0 - D13, A0 - A7). Not all of these pins are available, and there are limitations on some pins:

- D0 and D1 are used for the serial Tx/Rx pins and are therefore not available
- D2 - D13 are the digital pins which are all available
- A0 - A3 can be utilised as either digital or analogue pins
- A4 and A5 are reserved for the |I2C| interface and are therefore not available
- A6 and A7 can only be utilised as analogue inputs

This results in 18 pins total, with 2 pins (A6/A7) only available as analogue inputs, resulting in our defined total, minimum, and maximium values as seen on the :doc:`/ex-ioexpander/supported-devices` page:

.. list-table::
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

In the case we use the default of 12 digital pins and 6 analogue pins using the starting Vpin of 800, this will result in these Vpin allocations:

- Digital pins D2 - D13 as Vpins 800 - 811
- Analogue pins A0 - A3, A6 - A7 as Vpins 812 - 817

Once |EX-IO| has been configured as per the sections below, you can review the digial and analogue Vpin allocations by running the diag command ``<D HAL SHOW>`` at the serial console, which will display this information. Here is a sample output for EX-IOExpander on an Arduino Uno using the default 12 digital and 4 analogue pins:

.. code-block:: 

  <* EX-IOExpander I2C:x65 Configured on Vpins:800-815  *>
  <* EX-IOExpander x65 using driver version 0.0.1alpha *>
  <* EX-IOExpander x65: Digital Vpins 800-811, Analogue Vpins 812-815 *>

EX-CommandStation device driver
-------------------------------

To enable support for |EX-IO|, you need to configure "myHal.cpp" in your |EX-CS|. You will need to load the |EX-IO| device driver in addition to creating the device(s).

To create the |EX-IO| device, the syntax is `EXIOExpander::create(vpin, npins, address, digital_pins, analogue_pins);` where:

- vpin = An unused vpin
- npins = Total number of vpins to assign to the device (must equal digital_pins + analogue_pins)
- address = An available |I2C| address (default 0x65)
- digital_pins = The number of digital pins to enable
- analogue_pins = The number of analogue pins to enable

.. note:: 

  You need to ensure the total pins available for the device are assigned as either digital or analogue pins. Defining less or more than the total pins will result in a configuration error, and the device will be taken offline.

  If this occurs, you will see a message like this in the startup log: ``<* ERROR configuring EX-IOExpander device, I2C:x65 *>``

Refer to the :doc:`/ex-ioexpander/supported-devices` page to see the available pin numbers and predefined macros that are available for each of the supported devices.

In the example below, we will configure an Arduino Nano using the default pin counts at address 0x65, with an additional Arduino Uno device using all available digital capable pins and no analogue pins at address 0x66.

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

When :ref:`ex-ioexpander/overview:diag` is enabled, the configuration of each pin is displayed continuously to be able to monitor the configuration and state of each pin. By default, this will display every 3 seconds (3000ms). This configuration item allows the delay between updates to be increased or decreased.