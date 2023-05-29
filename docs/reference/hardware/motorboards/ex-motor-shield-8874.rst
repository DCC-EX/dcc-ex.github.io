.. include:: /include/include.rst
.. include:: /include/include-l3.rst
|donate-button|

********************************
DCC-EX EX-MotorShield8874 RevA
********************************

|conductor|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

Designed in conjunction with the |DCC-EX| development team, the EX-MotorShield8874 is extremely simple to use with all current and future generations of |EX-CS| hardware. It also safely powers the Command Station motherboard via the same single barrel jack DC input voltage that powers the track. It is rated at a very generous peak 5A of load per channel using Texas Instruments DRV8874 MOSFET technology. This board is the new standard by which we compare other boards.

.. image:: /_static/images/motorboards/ex_motorshield8874.jpeg
   :alt: DCC-EX EX-MotorShield8874 RevA Semify
   :scale: 10%

.. image:: /_static/images/motorboards/ex_motorshield8874_purple_side.jpg
   :alt: DCC-EX EX-MotorShield8874 RevA Millennium Engineering
   :scale: 10%

.. note:: 

   Whilst the EX-MotorShield8874 was designed by Semify who license it to manufacturers, the hardware design has graciously been made open source for individual users and the schematics are available on the `DCC-EX GitHub <https://github.com/DCC-EX/EX-Hardware/tree/main/EX-Motorshield8874>`_.

How can I get one?
==================

EX-MotorShield8874 is available immediately for purchase in the EU, USA and Canada via Semify's Tindie store (https://www.tindie.com/products/semify/semify-dcc-ex-motor-shield/) for $US34.90 each, and in Australia, New Zealand and South East Asia from Millennium Engineering Pty Ltd (orders @ milleng.com.au) for $AU55, plus shipping. It will also be available shortly in the UK through Chesterfield Model Making & Miniature Electronics (https://chesterfield-models.co.uk/product/semify-dcc-ex-motor-shield/), for £29.99 plus shipping. Expect further announcements re local availability in the US through DCC-EX directly and Smart Hobby LLC, with other countries to follow.

For quantities of 10 or less per annum, you may utilise a PCB manufacturing and assembly service such as JLCPCB without licensing fees. A donation to DCC-EX would be appreciated, so click the DONATE button! The production files are available on the `DCC-EX GitHub <https://github.com/DCC-EX/EX-Hardware/tree/main/EX-Motorshield8874>`_.

Entrepreneurs wanting to use the design to offer commercial quantities to their local communities should contact Semify (service @ semify-eda.com) to arrange a bulk purchase or DCC-EX (support @ dcc-ex.com) for a license to manufacture. Licensing includes donating a royalty to DCC-EX per board sold. Semify have been exempted from this due to their funding of the prototyping and work on verifying the design.

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
  **DO NOT** connect power to BOTH the EX-MotorShield8874 barrel jack and the underlying Arduino motherboard via its DC barrel jack as you may damage your Arduino and/or EX-MotorShield8874!!

The EX-MotorShield8874's DC barrel jack is the only power source required to power both the tracks and the |EX-CS| into which it is plugged. It supplies carefully regulated 7.2V DC power to the underlying Arduino R3 compatible motherboard via the VIN pin. This voltage is safely regulated down from the track power input to ensure Command Station motherboards will stay cool and work well. There is no need to power the Command Station via its barrel jack, or USB power. It is safe, however, to connect the USB cable as it will not create a conflict.

We suggest 10-12VDC for Z & N Scale, 14-16VDC for OO, HO, and 18-19VDC for O, or up to 24V for G scales because the EX-MotorShield8874 does not drop voltage like the standard L298 based motor shields. Note that good quality, fully-enclosed and double-insulated switch mode power supplies are best, and we suggest laptop power bricks as ideal in this role as they typically output 3-20A easily and safely.

.. note::
   Please note that as the EX-MotorShield8874 can supply up to 5A of track power per channel, a power supply of more than 10A peak capacity is required to run both channels at full peak current and have power left for the Command Station.

1. Turn on Power to the Motor Driver
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

Click :doc:`here </ex-commandstation/get-started/wifi-setup>` to learn how to connect the WiFi shield to your |EX-CS|, or *alternatively* connect a controller like |JMRI| or our |EX-WT| by using the serial cable to connect between your computer and the |EX-CS| as outlined in the :ref:`ex-installer/installing:1. getting ready` section of the |EX-I| page. Note that when configuring the EX-CommandStation you will want to select `EX8874_SHIELD` as the motor board during configuration.