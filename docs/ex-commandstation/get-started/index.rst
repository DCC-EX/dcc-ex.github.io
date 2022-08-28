.. meta::
   :keywords: EX-CommandStation Command Station EX-CS

.. include:: ../../include/include.rst
.. include:: ../../include/include-l2.rst
|EX-CS-LOGO|

***************
Getting Started
***************

|conductor| 

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

The following pages will instruct you on how to build an |EX-CS| including assembling your hardware, installing software, and running your first train. After that, we will provide examples for how the base system can be extended and upgraded.

What is EX-CommandStation?
==========================

An |EX-CS| is a simple, but powerful, DCC Command Station which you can assemble yourself and which is made using widely available Arduino boards. It supports much of the NMRA Digital Command Control (DCC) standards, including:

* Simultaneous control of multiple locomotives
* Control of all cab functions (F0-F28 and F29-F68)
* Control of accessory/function decoders (F0-F28 and F29-F68)
* Main Track: Write configuration variable (CV) bytes and set/clear specific CV bits (aka Programming on Main, or POM)
* Programming Track: Same as the main track with the addition of reading CV bytes

It includes advanced features such as:

* A |WiThrottle server| implementation, 
* General purpose inputs and outputs (I/O) for extensibility, and 
* |JMRI| integration

The Components of a Full System
================================

To actually run your model railroad you will need a few items:

.. image:: /_static/images/wifi/wangtongze_jumpered.png
   :alt: EX-CommandStation
   :scale: 15%
   :align: right

1. a |EX-CS| - This consists of:

  - an **Arduino microprocessor**,
  - a **Motor Driver** board / motor shield,
  - Optionally: 

    - a **WiFi shield (Recommended)** [#inst]_ (*This option is described on the following pages*), or
    - an ethernet shield, or
    - a Bluetooth board, or
    - direct connection to a PC [#jmri]_, and

  - our free, open source, custom software 

.. image:: /_static/images/engine_driver/vertical_slider.png
   :alt: Engine Driver
   :scale: 75%
   :align: right

1. a **Throttle (Controller)** - Something to control your trains with.  |BR| Such as our |EX-WT|, or other apps like |JMRI|, |Engine Driver|, |wiThrottle|, etc.
2. Power - The Arduino and the Motor shields need to be powered separately, so 
 
  - a **9-14v DC power supply** for the motor shield to the track, and 
  - a **5-9v DC power supply** for the Arduino

4. a **"Main" track,** aka "Operations" track - most people already have this: it's your layout!
5. a **"Programming" track,** aka "Service" track - an isolated short section of track that you will use to program locomotives
6. a **Train** - Specifically, a locomotive equipped with a DCC decoder (either a standard or sound decoder)

Next Steps - Purchasing Parts
=============================

Click :doc:`here <purchasing>` or click the "next" button to see what you need to aquire to create your |EX-CS|.

----

.. [#inst]  The Instructions on the following pages assume that that you will use a WiFi Shield.
.. [#jmri]  Requires |JMRI| installed on a computer.

.. toctree::
    :hidden:

    purchasing
    assembly
    wifi-setup
    installer
    controllers
    testing
    diagnosing-issues
