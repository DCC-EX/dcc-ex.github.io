.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-TT-LOGO|

**********
Purchasing
**********

|tinkerer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

What you need for EX-Turntable
==============================

* An |EX-CS| running the "add-turntable-controller" branch of `EX-CommandStation <https://github.com/DCC-EX/CommandStation-EX/tree/add-turntable-controller>`_ (this displays as version 4.0.2)
* An Arduino microcontroller (tested on Nano V3, both old and new bootloader, an Uno R3 should also work)
* A supported stepper motor driver and stepper motor (see list below)
* A hall effect (or similar) sensor for homing, which needs to be digital/unipolar such as an A3144 or 44E (or equivalent)
* A suitable power supply - note that your chosen stepper driver/motor will dictate this, see note below
* A prototyping shield is highly recommended, especially when using a Nano, and the pictured version is preferred over the screw terminal version
* Dupont type wires to connect the components, male to female or female to female as required
* A USB cable to connect the Arduino to a PC to load the software
* *Optional:* A dual relay board (or similar) if you wish to use the phase switching capability (see :ref:`ex-turntable/overview:important! phase (or polarity) switching`)

.. note:: 

  If you wish to make use of the traverser feature, there is further information on what is required to enable this on the :doc:`/ex-turntable/traverser` page.

.. image:: /_static/images/turntable-ex/nano-v3.png
  :alt: Nano V3
  :scale: 50%

.. image:: /_static/images/turntable-ex/uln2003-28byj-48.png
  :alt: ULN2003/28BYJ-48 Stepper combo
  :scale: 50%

.. image:: /_static/images/turntable-ex/hall-effect.png
  :alt: Hall Effect sensor
  :scale: 40%

.. image:: /_static/images/turntable-ex/dual-relay.png
  :alt: Dual Relay
  :scale: 40%

.. image:: /_static/images/turntable-ex/nano-shield1.png
  :alt: Nano Prototype Shield
  :scale: 40%

.. image:: /_static/images/turntable-ex/dupont.png
  :alt: Dupont male to female
  :scale: 30%

Power supplies
--------------

Choosing the right power supply for your Arduino and stepper motor is important to get right.

If you are using the default ULN2003/28BYJ-48 it is technically possible to power the driver and stepper directly from the 5V output on an Arduino, however this is not recommended and should be avoided.

Given that this combo requires 5V, you can use a single, regulated 5V DC power supply rated for at least 500mA to power both the Arduino and the ULN2003/28BYJ-48.

Note that if you use the right Arduino Nano prototyping shield, it will likely have a LM317 voltage regulator supplied by the DC power jack. In this instance, you can use a 7 to 9V 500mA+ DC power supply to provide power, and it will be safe to connect the ULN2003 5V to a 5V output on the prototyping shield.

For other steppers such as the NEMA17 that require 12V DC, you will need either two separate power supplies, or a DC-DC converter to provide a lower voltage to the Arduino. Note that the NEMA17 steppers have a considerably higher current rating, so the power supply will need to be rated at 1.5A or higher.

Supported stepper drivers and motors
=========================================

The default configuration of |EX-TT| is for the ubiquitous ULN2003/28BYJ-48 stepper driver and motor combination. These steppers are used in a myriad of applications, are inexpensive, and will be suitable for most smaller scale turntable applications.

.. sidebar:: Unsupported stepper drivers and motors

 |tinkerer|

  If you have a need to use a different driver, these should be relatively straight forward to configure in a similar manner to how additional motor drivers are configured for use with CommandStation-EX.

  Refer to :ref:`ex-turntable/configure:defining custom stepper drivers` for more details.

However, it is very easy to use one of several other common stepper drivers if you require more torque, or if you prefer to use a NEMA17 or other stepper motor.

The complete list of supported stepper drivers and motors:

* ULN2003/28BYJ-48 (Default)
* A4988/NEMA17
* DRV8825/NEMA17

Next Steps
==========

Now that you know what you need, click the "next" button see what is needed to create an |EX-TT|.