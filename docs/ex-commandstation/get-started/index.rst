.. include:: /include/include.rst
.. include:: /include/include-l2.rst
**********************************
Getting Started - Purchasing Parts
**********************************

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

|conductor| 

This following pages will instruct you on how to build an |EX-CS| including assembling your hardware, installing software, flashing firmware, and running your first train. After that, we will provide examples for how the base system can be extended and upgraded.

What is EX-CommandStation?
==========================

A basic |EX-CS| hardware setup can be made from easy to find, widely available, Arduino boards that you can assemble yourself. It supports much of the NMRA Digital Command Control (DCC) standards, including:

* simultaneous control of multiple locomotives
* Activate/de-activate all accessory function addresses 0-2048
* Control of all cab functions F0-F28 and F29-F68
* Main Track: Write configuration variable (CV) bytes and set/clear specific CV bits (aka Programming on Main, or POM)
* Programming Track: Same as the main track with the addition of reading CV bytes

It includes advanced features such as:

* A WiThrottle server implementation, 
* Turnout operation, 
* General purpose inputs and outputs (I/O) for extensibility, and 
* JMRI integration

The Components of a Full System
================================

To actually run your model railroad you will need a few items:

1. a |EX-CS| - This consists of:

  - an Arduino microprocessor,
  - a motor driver board / motor shield,
  - (Optionally) 
    
    - a WiFi shield (Recommended), or
    - an ethernet shield, or
    - neither [#jmri]_, and

  - our free, open source, custom software 
 
2. a **Controller (Throttle)** - Something to control you trains with.  |BR| Such as our |EX-WT|, or other apps like JMRI, Engine Driver, wiThrottle, etc
#. **Power** - The Arduino and the Motor shields need to be powered separately, so a DC power supply for the motor shield to the track, and one for the Arduino
#. a **"Main" track,** aka "Operations" track - most people already have this: it's your layout!
#. a **"Programming" track,** aka "Service" track - an isolated short section of track that you will use to program locomotives
#. a **Train** - Specifically, a locomotive equipped with a DCC decoder (either a standard or sound decoder)

.. [#jmri]  Requires JMRI installed on a computer

What you need
=============

.. sidebar::  Optional configuration
    
  |conductor|

  |EX-CS| can be configured in several additional 'Conductor friendly' ways.

  - without wifi or ethernet - requires JMRI installed on a computer
  - with a supported :doc:`Ethernet shield </reference/hardware/ethernet-boards>` instead of the WiFi shield

  |tinkerer| |engineer|

  |EX-CS| is also supported on a variety of different hardware that you might also consider

  - Supported :doc:`Arduino boards </reference/hardware/microcontroller-boards>`
  - Supported :doc:`motor shields </reference/hardware/motor-boards>`
  - Supported :doc:`ESP8266 WiFi shield </reference/hardware/wifi-boards>`
  - Supported :doc:`Ethernet shield </reference/hardware/ethernet-boards>`


Hardware
________

You will need to find or purchase:

- a supported **Arduino board**. |BR| We recommend the ???
- a supported **motor shield**.  |BR| We recommend the ???
- a 9-14v DC :doc:`power supply </reference/hardware/power-supplies>` for the motor shield
- a supported **WiFi shield**. |BR| We recommend the ???
- a **7-9v DC power supply** for the Arduino (while it is connected to the PC, this is not needed)
- a **computer** running Windows, macOS, or Linux (even a Raspberry Pi)
- a **USB Cable** from the computer to the Arduino
- a **piece of track** to run trains or program on
- a known-working **DCC-equipped locomotive**


See this :doc:`Shopping List </reference/hardware/shopping-list>` for everything you need, organized for you in one place.

Software
________

The |EX-I| is recommended for most users as it automatically downloads and installs the required software. 

- See the :doc:`Command Station download page </download/ex-commandstation>` to download a copy to your computer.

A Controller (Throttle)
_______________________


You'll also need something to control your trains. Because there are several options, we will discuss this following the system setup.


I'm Ready!
===========

Click the "next" button to see how to assemble your |EX-CS|.

.. toctree::
    :hidden:

    assembly
    wifi-setup
    installer
    arduino-ide
    controllers
    diagnosing-issues
