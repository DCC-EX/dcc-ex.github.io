.. meta::
  :keywords: EX-CommandStation Command Station EX-IOExpander

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-IO-LOGO|

**************************
Overview and configuration
**************************

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

There is also work in progress to enable using PWM capable pins to drive servos and control LED brightness.

Rather than emulate any specific type of existing I/O expander, |EX-IO| has been written to integrate directly with |EX-CS| via its own device driver, which is how both digital and analogue pins can easily be utilised on the same device.

This page provides the general overview of |EX-IO|, as well as outlining the configuration options available.

.. note:: Credits

  |EX-IO| was inspired by the work of Mike B (@Springlake on Discord) and Ross (@Rosscoe on Discord) to emulate an MCP23017 device as part of a mimic panel design. The DCC-EX team have taken this inspiration and now provide a generic Arduino based I/O expander, able to utilise both digital and analogue pins.

Software requirements
=====================

To utilise |EX-IO|, you must be running the latest unreleased Development version of |EX-CS|.

Refer to :ref:`download/ex-commandstation:latest ex-commandstation unreleased development version` on how to obtain this.

In addition, you will require the |EX-IO| software which can be found here:

.. rst-class:: dcclink

  `EX-IOExpander Github Repository <https://github.com/DCC-EX/EX-IOExpander>`_

Hardware requirements
=====================

|EX-IO| needs a dedicated microcontroller connected to the |I2C| bus of your |EX-CS|.

Refer to :doc:`/ex-ioexpander/supported-devices` for the currently supported microcontrollers, which includes details on the pins and features available for use.

The device driver and |EX-IO| software are being written in such a way that should enable porting to other microcontroller architectures, and is expected to support up to 256 I/O pins. As more devices are tested and/or requested, additional devices will be supported.

Theory of operation
===================

|EX-IO| can utilise digital pins in both input and output mode, and analogue pins in input mode. Digital pins in input mode can have pullups enabled or disabled.

Pins capable of both digital and analogue can be used for either purpose.

As per other I/O devices, |EX-IO| can function with both the ``<S ...>`` sensor/input and ``<Z ...>`` output |DCC-EX| commands, as well as the various ``AT(), IF(), ATGTE(), IFGTE()`` type |EX-R| commands.

The work currently in progress will allow PWM capable pins to be used to drive servos and control LED brightness, enabling use of the ``<D SERVO ...>`` command, along with the ``SERVO()``, ``SERVO_TURNOUT()``, ``SERVO_SIGNAL()``, and ``FADE()`` |EX-R| commands.

.. note:: 

  To ensure the devices start with I/O pins in the safest possible state, all defined pins are set to input mode with pullups disabled by default. The pins stay in this state until they are configured explicitly via the |EX-CS| device driver.

Configuration
=============

Aside from configuring the |I2C| address of your |EX-IO| device, the device driver loaded in your |EX-CS| will perform the necessary run time configuration at startup, meaning you should only ever need to update the |EX-IO| software when a new version is available.

Configuration changes for |EX-IO| are made by editing a "myConfig.h" file or writing to EEPROM if supported. An example "myConfig.example.h" file is included that can be copied and edited to suit. The only configuration item you should really need to consider is :ref:`ex-ioexpander/overview:i2c_address`.

Software installation process
-----------------------------

This is a brief overview of the software installation and configuration process:

1. Download the "main" branch of |EX-IO|
2. If running Nucleo or any other device without EEPROM, copy "myConfig.example.h" to "myConfig.h" and set the |I2C| address
3. Upload |EX-IO| to your Arduino (note, this does not get uploaded to your CommandStation)
4. For Arduino Nano, Uno, or Mega, use the serial console to set the |I2C| address
5. Download the "devel" branch of |EX-CS|
6. Configure "config.h", "myHal.cpp", and apply any required configuration changes
7. Upload |EX-CS| to your CommandStation

Configure I2C address via serial
--------------------------------

For devices with EEPROM support (Arduino Uno, Nano, and Mega), it is possible to configure the |I2C| address via the serial console rather than having to update "myConfig.h", and therefore you should be able to simply upload the software without needing to edit any files at all.

Be aware that this address will override any address defined in "myConfig.h", and if using these devices, you do not need a "myConfig.h" file at all for normal operation.

.. warning:: 

  Using the reboot ``<Z>`` command on an Arduino Nano with the old bootloader will cause it to enter into an endless reboot cycle, requiring a power cycle to recover. Pressing the reset button will not recover from the condition. Nanos with the new bootloader are fine with this command.

  When using the old bootloader, use the reset button rather than the ``<Z>`` command to reboot.

There are three serial commands available to set, read, and erase the configured address, with an additional command to reboot the device:

.. list-table::
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Command
    - Purpose
  * - <W address>
    - This command writes the |I2C| address to EEPROM, for example <W 50> will set it to 0x50
  * - <R>
    - This will read and display the |I2C| address stored in EEPROM
  * - <E>
    - This will erase the |I2C| address stored in EEPROM
  * - <Z>
    - This will reboot to allow activating address changes

Pin/Vpin allocation
-------------------

.. note:: 

  It has been reported that on non-genuine Arduino Uno devices (and potentially Nano) using pin D13 as an input may not work as expected due to the onboard LED causing the pin to remain low when using it as an input pin with pullups enabled. A suggested workaround is to add an external 1K pullup resistor to 5V for this pin if this is experienced.

When configuring your chosen |EX-IO| device, you need to know the total number of available pins, and the capability of each. Details of the pins available for use are outlined on the :doc:`/ex-ioexpander/supported-devices` page. Vpins are allocated by the |EX-CS| device driver in ascending order according to the device map on this page.

.. note:: 

  When the |EX-IO| device receives its configuration from the |EX-CS|, the Vpin to physical pin map will be displayed in the serial console of the |EX-IO| device.

For example, an Arduino Nano has a total of 22 I/O pins (D0 - D13, A0 - A7). Not all of these pins are available, and there are limitations on some pins:

- D0 and D1 are used for the serial Tx/Rx pins and are therefore not available
- D2 - D13 are the digital pins which are all available
- A0 - A3 can be utilised as either digital or analogue pins
- A4 and A5 are reserved for the |I2C| interface and are therefore not available
- A6 and A7 can only be utilised as analogue inputs

This results in 18 pins total, with 2 pins (A6/A7) only available as analogue inputs, resulting in our pin counts and Vpin to pin map as seen on the :doc:`/ex-ioexpander/supported-devices` page:

.. list-table:: Arduino Nano pin allocations
  :widths: auto
  :stub-columns: 1
  :class: command-table

  * - Total pins
    - 18
  * - Digital capable pins
    - 16
  * - Analogue capable pins
    - 6
  * - PWM capable pins
    - 6

.. csv-table:: Arduino Nano and Pro Mini EX-IOExpander pin map at Vpin 800
  :widths: auto
  :header-rows: 1

  Vpin,Pin,Digital,Analogue,PWM
  800,2,Y,N,N
  801,3,Y,N,Y
  802,4,Y,N,N
  803,5,Y,N,Y
  804,6,Y,N,Y
  805,7,Y,N,N
  806,8,Y,N,N
  807,9,Y,N,Y
  808,10,Y,N,Y
  809,11,Y,N,Y
  810,12,Y,N,N
  811,13,Y,N,N
  812,A0,Y,Y,N
  813,A1,Y,Y,N
  814,A2,Y,Y,N
  815,A3,Y,Y,N
  816,A6,N,Y,N
  817,A7,N,Y,N

Once |EX-IO| has been configured as per the sections below, you can review the digial and analogue Vpin allocations by running the diag command ``<D HAL SHOW>`` at the serial console, which will display this information.

This sample output is for EX-IOExpander on an Arduino Nano at the default 0x65 address using the default 12 digital and 8 analogue pins, and an Arduino Uno at 0x66 using all 16 pins as digital pins:

.. code-block:: 

  <* EX-IOExpander I2C:x65 v0.0.6: 12 Digital Vpins 800-811, 6 Analogue Vpins 812-817  *>
  <* EX-IOExpander I2C:x66 v0.0.6: 16 Digital Vpins 820-835, 0 Analogue Vpins 0-0  *>

EX-CommandStation device driver
-------------------------------

To enable support for |EX-IO|, you need to configure "myHal.cpp" in your |EX-CS|. The device driver is included by default, so you simply need to create the device(s).

.. note:: 

  For those using earlier releases of this device driver, the default pin macros (eg. EXIO_NANO_ANALOGUE_PINS) have been removed to simplify adding support for new devices.

You will find an example included in the "myHal.cpp_example.txt" file included with the |EX-CS| software.

To create the |EX-IO| device, the syntax is `EXIOExpander::create(vpin, npins, address, digital_pins, analogue_pins);` where:

- vpin = An unused vpin
- npins = Total number of vpins to assign to the device (must equal digital_pins + analogue_pins)
- address = An available |I2C| address (default 0x65)
- digital_pins = The number of digital pins to enable
- analogue_pins = The number of analogue pins to enable

.. note:: 

  You need to ensure the total pins available for the device are assigned as either digital or analogue pins. Defining less or more than the total pins will result in a configuration error, and the device will be taken offline.

  If this occurs, you will see a message like this in the startup log: ``<* ERROR configuring EX-IOExpander device, I2C:x65 *>``

Refer to the :doc:`/ex-ioexpander/supported-devices` page to see the available pin numbers for each of the supported devices.

In the example below, we will configure an Arduino Nano using the default pin counts at address 0x65, with an additional Arduino Uno device using all available digital capable pins and no analogue pins at address 0x66 (note this is what provides the output seen in the previous section).

.. code-block:: cpp

  void halSetup() {
    ...
    EXIOExpander::create(800, 18, 0x65, 12, 8);
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

If the device has EEPROM support, and a valid address is defined in EEPROM, the address defined in EEPROM will always override the address defined in "myConfig.h".

DIAG
----

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Uncomment to enable diag output
  // 
  // #define DIAG

Uncommenting this line will enable extra diagnostic output to the serial console to help with diagnosis and troubleshooting in the event issues are encountered.

You can also configure this via the serial console using the ``<D>`` command (see :ref:`ex-ioexpander/testing:diagnostic commands`).

DIAG_CONFIG_DELAY
-----------------

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Delay between dumping the status of the port config if DIAG enabled
  // 
  #define DIAG_CONFIG_DELAY 5

When :ref:`ex-ioexpander/overview:diag` is enabled, the configuration of each pin is displayed continuously to be able to monitor the configuration and state of each pin. By default, this will display every 5 seconds. This configuration item allows the delay between updates to be increased or decreased.

You can also configure this via the serial console using the ``<D delay>`` command (see :ref:`ex-ioexpander/testing:diagnostic commands`).

TEST_MODE
---------

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Enable test mode - ensure only one test mode is active at one time.
  //  This is handy if serial input doesn't work for commands for some reason. 
  // 
  //  ANALOGUE - equivalent of <A>
  //  INPUT - equivalent of <I>
  //  OUTPUT - equivalent of <O>
  //  PULLUP - equivalent of <P>
  // 
  // #define TEST_MODE ANALOGUE_TEST
  // #define TEST_MODE INPUT_TEST
  // #define TEST_MODE OUTPUT_TEST
  // #define TEST_MODE PULLUP_TEST

If for some reason serial input is not working as expected, test modes can be enabled via this option in "myConfig.h".

Only enable one test mode at a time. If multiple are enabled, only the last one defined will take effect.

Refer to :ref:`ex-ioexpander/testing:testing commands` for details on the testing each option enables.

DISABLE_I2C_PULLUPS
-------------------

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Uncomment to disable internal I2C pullup resistors
  //  NOTE: This will not apply to all supported devices, refer to the documentation
  // #define DISABLE_I2C_PULLUPS

In cases where multiple |I2C| devices exist on the same bus, the pullup resistors may cause issues with reliability even the resultant resistance across all devices is too low (see :ref:`reference/hardware/i2c-devices:pull-ups`).

In these instances, if the |EX-IO| device does not have physical, external pullup resistors, the internal software pullups can be disabled by uncommenting this line.

Some devices such as the Arduino Mega2560 have physical pullup resistors on the |I2C| pins, and therefore this configuration setting will have no effect on these devices.