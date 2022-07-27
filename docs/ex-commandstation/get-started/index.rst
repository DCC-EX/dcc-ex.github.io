.. include:: /include/include.rst
.. include:: /include/include-l2.rst
***************
Getting Started
***************

|conductor| 

This next few page will instruct you on how to build an |EX-CS| including assembling your hardware, installing software, flashing firmware, and running your first train. After that, we will provide examples for how the base system can be extended and upgraded.

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

#. An |EX-CS| - This consists of:

  - An Arduino microprocessor,
  - a motor driver board / motor shield,
  - (Optionally) a WiFi shield, and
  - our free, open source, custom software 
 
#. A **Controller** - Something to control you trains with.  |BR| Such as our |EX-WT|, or other apps like JMRI, Engine Driver, wiThrottle, etc
#. **Power** - The Ardunio and the Motor shields need to be powered separately, so a DC power supply for the motor shield to the track, and one for the Arduino
#. A **"Main" track,** aka "Operations" track - most people already have this: it's your layout!
#. A **"Programming" track,** aka "Service" track - an isolated short section of track that you will use to program locomotives
#. A **Train** - Specifically, a locomotive equipped with a DCC decoder (either a standard or sound decoder)


What you need
==============

.. sidebar::  |tinkerer| |engineer|

  |EX-CS| is supported on a variety of different hardware that you might also consider

  - Supported :doc:`Arduino boards </reference/hardware/microcontroller-boards>`
  - Supported :doc:`motor shields </reference/hardware/motor-boards>`

**Hardware**:

- Supported Arduino board.  We recommend the ???
- Supported moto shield.  We recommend the ???
- Compatible :doc:`power supply </reference/hardware/power-supplies>`
- Computer running Windows, macOS, or Linux (even a Raspberry Pi)
- USB Cable from the computer to the Arduino
- Piece of track to run trains or program on
- Known-working DCC-equipped locomotive

**Optional hardware**:

- Supported :doc:`ESP8266 WiFi shield </reference/hardware/wifi-boards>`
- Supported :doc:`Ethernet shield </reference/hardware/ethernet-boards>`

**Software**:

- See the :doc:`Command Station download page </download/ex-commandstation>`

The |EX-I| is recommended for most users as it automatically downloads and installs the required software. 

You'll also need something to control your trains. Because there are several options, we will discuss this following the system setup.

See this :doc:`Shopping List </reference/hardware/shopping-list>` for everything you need, organized for you in one place.

I'm Ready!
===========

Click the "next" button below to choose your path, and then move ahead to how to assemble your Command Station.

.. toctree::
    :hidden:

    assembly
    wifi-setup
    installer
    arduino-ide
    controllers
    diagnosing-issues
