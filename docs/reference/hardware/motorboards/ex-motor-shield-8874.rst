.. include:: /include/include.rst
.. include:: /include/include-l3.rst
********************************
DCC-EX EX-MotorShield8874 RevA
********************************

|conductor|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

Designed in conjunction with the |DCC-EX| development team, the EX-MotorShield8874 is extremely simple to use with all generations of |EX-CS| hardware. It also powers the Command Station motherboard via the same single barrel jack DC input voltage that powers the track. It is rated at a very generous true 5A of load per channel and does not require a heatsink or fan as it runs cool due to the Texas Instruments DRV8874 MOSFET technology. This board is the new standard by which we compare other boards.

.. image:: /_static/images/motorboards/ex_motorshield8874.jpeg
   :alt: DCC-EX EX-MotorShield8874 RevA Semify
   :scale: 10%

.. image:: /_static/images/motorboards/ex_motorshield8874_purple_side.jpg
   :alt: DCC-EX EX-MotorShield8874 RevA Millennium Engineering
   :scale: 10%

.. note:: 

   While this board is designed by and licensed to Semify, the hardware design has graciously been made open source and the schematics are available on the `Semify GitHub <https://github.com/semify-eda/motor-shield/blob/main/motor-shield.pdf>`_.

How can I get one?
==================

For quantities of 10 or less, you may utilise a service such as JLCPCB without licensing fees payable to Semify blah blah blah

You can purchse from... blah blah blah

Add note here on license terms with Semify, dontation to DCC-EX etc.

Assembly with EX-MotorShield8874
================================

Aseembly with the EX-MotorShield8874 is extremely simple, just plug the motor shield into your choice of Command Station motherboard.  Unlike other motor shields, the EX-MotorShield8874 needs no jumpering, trace cutting, or pin bending! Just plug it in.

Shown here are examples of the shield plugged into Mega+WiFi, Nucleo-F411RE:

.. image:: /_static/images/motorboards/ex_motorshield8874_mega.jpg
   :alt: DCC-EX EX-MotorShield8874 RevA on Mega+WiFi
   :scale: 15%

.. image:: /_static/images/motorboards/ex_motorshield8874_nucleo_f411.jpg
   :alt: DCC-EX EX-MotorShield8874 RevA on Nucleo-F411RE
   :scale: 15%
      

Example pics here!

1. Connect DC Power to Motor Driver
------------------------------------

The EX-MotorShield8874 accepts a standard 2.5mm DC barrel jack for DC power, with centre pin positive, and polarity protected for your safety. Acceptable voltages for correct DCC operation include 10-24VDC, but the shield can cope with 9-30VDC.

.. image:: /_static/images/motorboards/ex_motorshield8874_purple_megawifi.jpg
   :alt: DCC-EX EX-MotorShield8874 RevA on Mega+WiFi with power and track connectors
   :scale: 10%
   

.. note::
  **DO NOT** connect power to the underlying Arduino motherboard via its DC barrel jack as you may damage your Arduino and/or EX-MotorShield8874!! <BR> The EX-MotorShield8874 supplies power to the underlying |EX-CS| via the VIN pin. This voltage is carefully regulated on the EX-MotorShield8874 to a safe 7.2VDC which will mean all Command Station motherboards will stay cool and work well. There is no need to power the Command Station via its barrel jack, or USB power. It is safe, however, to connect the USB cable as it will not create a conflict.

We suggest 10-12VDC for Z & N Scale, 14-16VDC for OO, HO, and 18-19VDC for O, or up to 24V for G scales because the EX-MotorShield8874 does not drop voltage like the standard L298 based motor shields. Note that good quality, fully-enclosed and double-insulated switch mode power supplies are best, and we suggest laptop power bricks as ideal in this role as they typically output 3-20A easily and safely.

.. note::
   Please note that as the EX-MotorShield8874 can supply up to 5A of track power per channel, a power supply of more than 10A capacity is required to run both channels at full current and have power left for the Command Station.

2. Turn on Power to the Motor Driver
------------------------------------

Once satisfied the EX-MotorShield8874 is seated properly on the Command Station motherboard, you can apply power to the |EX-CS|. You ought to see a green LED light up indicating power is being supplied to the motherboard.

.. image:: /_static/images/motorboards/ex_motorshield8874_purple_megawifi_LED_on.jpg
   :alt: DCC-EX EX-MotorShield8874 RevA on Mega+WiFi with power LED on
   :scale: 10%
   

3. Connect Track to Motor Driver
------------------------------------

Track power for A (MAIN) and B (PROG) tracks can be connected now using the green track connectors. These unplug conveniently to allow easy swapping in and out of the |EX-CS|. Make sure to tighten the screws onto the wire in the connectors before applying power.

.. image:: /_static/images/motorboards/ex_motorshield8874_purple_connector_closeup.jpg
   :alt: DCC-EX EX-MotorShield8874 RevA connectors
   :scale: 30%
   
Notice that A (MAIN) is on the left as you look at the connectors, and B (PROG) is on the right, next to the DC barrel jack.

Next steps
==========

Click :doc:`here </ex-commandstation/get-started/wifi-setup>` to learn how to connect the WiFi shield to your |EX-CS|, or *alternatively* connect a controller like |JMRI| or our |EX-WT| by using the serial cable to connect between your computer and the |EX-CS| as outlined in the :ref:`ex-installer/installing:1. getting ready` section of the |EX-I| page.
