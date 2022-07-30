.. include:: /include/include.rst
.. include:: /include/include-l2.rst
****************
Purchasing Parts
****************

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

|conductor| 

This page explains what you will need to acquire to build a |EX-CS| using the recommended parts for a |conductor-text|.  

Some of the parts (like track and some wire) you will likely already have on hand.

|force-break|

What you need to purchase or find
=================================

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

#. a supported **Arduino board** |BR| We recommend the *Elegoo Mega 2560* |BR| |BR|
#. a supported **motor shield**  |BR| We recommend the *Deek-Robot Motor Shield* |BR| |BR|
#. a supported **WiFi shield** |BR| We recommend the *Makerfabs ESP8266 WiFi Shield* |BR| |BR|
#. Two (2) Male to Female **Jumpers leads** |BR| |BR|
#. a 9-14v DC :doc:`power supply </reference/hardware/power-supplies>` for the motor shield |BR| |BR|
#. a 2.5mm x 5.5mm Female DC Plug to **Screw Terminal (optional, but recommended)** to connect the motor shield power supply |BR| |BR|
#. a **7-9v DC power supply** |BR| for the Arduino (while it is connected to the PC, this is not needed) |BR| |BR|
#. any **computer** running Windows, macOS, or Linux (only needed for the initial install of the software) |BR| |BR|
#. a **USB Cable** from the computer to the Arduino |BR| |BR|
#. a **piece of track** to run trains or program on |BR| |BR|
#. some **wire** (18 to 16 AWG twisted pair recommended. See Technical Note below) |BR| |BR|
#. a known-working **DCC-equipped locomotive**


XXXXX See this :doc:`Shopping List </reference/hardware/shopping-list>` for everything you need, organised for you in one place.

Software
________

Our |EX-I| app is recommended for most users as it automatically downloads and installs the required software. 

13. See the :doc:`Command Station download page </download/ex-commandstation>` to download a copy to your computer.

A Controller (Throttle)
_______________________


14. You'll also need something to control your trains. |BR| There are several options. We will discuss these following the system setup, but the introductory configuration covered in the following pages lends itself to using a smart phone (Android or Apple iOS).

Next Steps
==========

Click the "next" button to see how to assemble your |EX-CS|.

.. note::

   **TECHNICAL NOTES**

   **Wire Gauge** - The Arduino motor controller can only provide about 1.5 Amps of power (despite being rated for 2A), so 18 AWG wire is ample. If you use a different motor controller and deliver more current to your track, you may need thicker wire (lower number gauge).
