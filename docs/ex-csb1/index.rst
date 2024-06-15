:orphan:

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-cs.rst
  
|EX-CS-LOGO| |donate-button|

.. index:: EXCSB1, EX-CSB1

******************
EX-CSB1 Express
******************

|conductor| |tinkerer| |engineer| |support-button|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

Designed by the |DCC-EX| development team, the |EX-CSB1|replaces up to 3 different stacked board with one is extremely simple to use  XXX -fnd fix

.. figure:: /_static/images/motorboards/ex_motorshield8874.png
   :alt: DCC-EX EX-MotorShield8874 RevA Semify
   :scale: 10%

What is EX-CSB1 Express?
==========================

The EX-CSB1 is the first complete DC and DCC command station and/or Booster from the DCC-EX Team. That's right, one board that can function as full USB or WiFi Wireless command station that can include an optional booster, or itself operate as a stand-alone booster elsewhere on your layout! There really is nothing else like it on the market. The EX-CSB1 saves you money while allowing you to more easily expand your layout.

* All-in-one compatible Command Station/Booster
* Built-in graphical OLED display for status and diagnostics (extra displays can be added)
* ESP32 fast 32-bit microcontroller with built-in WiFi for up to 10 simultaneous throttle connections (more with JMRI)
* Runs DCC-EX Command Station Software (free)
* Runs DC or DCC trains
* More memory for larger EXRAIL automation/animation scripts than an Arduino Mega
* Dual DCC or PWM DC 5A outputs and variable limit software to control current to the tracks
* Only one 12V to 25V power supply required to power the command station and the tracks!
* Over-current protection per output
* Railsync DCC signal input for booster mode
* Accepts EX-MotorShield8874 for additional 2 DCC/DC PWM/PROG outputs
* DC outputs for 4 total power districts!
* USB-C connection for software updates, connection to EXWebThrottle or JMRI, and full logging/debugging
* Qwiic/STEMMA QT compatible I2C connector foraccessories like displays, turnouts, lighting, etc.
* Short circuit protection for both tracks and reverse voltage input protection
* Dynamically assign any output to programming mode, with NMRA current limit enforced
* DCC Booster mode automatically engaged on receipt of a Railsync DCC input signal
* TrackManager :sup:`tm` support for configuring any output to any one of the DC/DCC/Prog modes

The EX-CSB1 Express is based on a 32-bit ESP32 processor that operates on 3.3V rather than 5V for increase efficiency and more options for powering the board. It uses a robust, single-PCB design with dual outputs to provide an expandible Command Station and/or Booster in a small portable form factor.

The EX-CSB1 comes with two integrated MOSFET based motor drivers from Texas Instruments to reduce power consumption and generate less heat than traditional solutions. They provide pow

T

Powering of Arduino boards is possible due to the on board DC/DC buck converter, supporting a wide input supply range from 9 to 30V. The reverse polarity protection prevents damage to the circuit and its components in case the power supply is accidentally connected backwards.

The board's 5V and 3V3 friendly design makes it suitable for a broad range of Arduino compatible platforms, with an override that compensates for designs with incomplete support (such as an incorrect IORef voltage).

This Shield features a status LED for supply, which provides a visual indication of the power supply status in addition to LEDs to show each side of the A and B power outputs.


XXX - use some of this -fnd

CONTROL YOUR ENTIRE LAYOUT,
INCLUDING DCC AND DC LOCOMOTIVES
AND ACCESSORIES, WITH THE EX-CSB1
AND EXRAIL AUTOMATION and Animation capability

That’s right, one board that can
be configured as a full
Command Station or a dual
output 5A booster! Expandible
to 2 more outputs simply by
adding an EX-MotorShield8874
on top. That’s 4 5A power districts to control even large layouts.
Still need more? Use more EX-CSB1s as boosters and spread them
around the layout connected by the Railsync port.

Why did we make it?
====================

EX-Motorshield8874 is specifically designed for use with DCC-EX Command Station for controlling model railroads, but can also be used as generally better replacement for Arduino Motor Shield R3 in any device that needs to control a motor. We needed higher current capacity to power more motors/trains and have little to no voltage 

How can I get one?
==================

Units may be purchased from the following sources:

* In the US from the `DCC-EX Store <https://store.dcc-ex.com/>`_ or...
* from `Smart Hobby, LLC <https://www.smarthobbyllc.com/>`_. You can also find Smart Hobby on Facebook
* In the UK from `Chesterfield Model Making & Miniature Electronics <https://chesterfield-models.co.uk/product/semify-dcc-ex-motor-shield/>`_
* In Europe from `Semify's Web Store <https://www.semify-eda.com/ex-motorshield8874/>`_ (based in Austria)
* In Australia, New Zealand and South East Asia from `Millennium Engineering Pty Ltd <https://www.milleng.com.au>`_
* and other manufacturers licensed by DCC-EX.

There are different options for the board such as with or without an EX-MotorShield 8874 for two additional outputs. Prices vary from around $105-$145 in the US, to approximately £ XXX -fnd in the UK, € XXX -fnd in Europe, and in Australia starting from $AU XXX -fnd. Prices typically do not include tax and shipping.

Ordering in Quantity or wishing to Resell
==========================================

For quantities of 10 or less per annum, you may utilise a PCB manufacturing and assembly service such as JLCPCB without licensing fees. A donation to DCC-EX would be appreciated, so click the DONATE button! The production files are available on the `DCC-EX GitHub <https://github.com/DCC-EX/EX-Motorshield8874>`_.

Entrepreneurs wanting to use the design to offer commercial quantities to their local communities should contact DCC-EX (sales @ dcc-ex.com) to arrange a bulk purchase or a license to manufacture. Licensing includes donating a royalty to DCC-EX per board sold.


DCC and DC Operation
=====================

Integrated displays
====================

