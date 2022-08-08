.. meta::
   :keywords: EX-CommandStation Command Station

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|

***************
Getting Started
***************

|conductor| 

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

The following pages will instruct you on how to build an |EX-CS| including assembling your hardware, installing software, flashing firmware, and running your first train. After that, we will provide examples for how the base system can be extended and upgraded.

What is EX-CommandStation?
==========================

A basic |EX-CS| can be made from widely available Arduino boards that you can assemble yourself. It supports much of the NMRA Digital Command Control (DCC) standards, including:

* Simultaneous control of multiple locomotives
* Control of all cab functions (F0-F28 and F29-F68)
* Control of accessory/function decoders (F0-F28 and F29-F68)
* Main Track: Write configuration variable (CV) bytes and set/clear specific CV bits (aka Programming on Main, or POM)
* Programming Track: Same as the main track with the addition of reading CV bytes

It includes advanced features such as:

* A WiThrottle server implementation, 
* General purpose inputs and outputs (I/O) for extensibility, and 
* |JMRI| integration

The Components of a Full System
================================

To actually run your model railroad you will need a few items:

1. a |EX-CS| - This consists of:

  - an **Arduino microprocessor**,
  - a **Motor Driver** board / motor shield,
  - Optionally: 
    
    - a **WiFi shield (Recommended)** [#inst]_, or
    - an ethernet shield, or
    - neither [#jmri]_, and

  - our free, open source, custom software 
 
2. a **Controller (Throttle)** - Something to control you trains with.  |BR| Such as our |EX-WT|, or other apps like |JMRI|, |Engine Driver|, |wiThrottle|, etc
#. Power - The Arduino and the Motor shields need to be powered separately, so 
 
  - a **9-14v DC power supply** for the motor shield to the track, and 
  - a **5-9v DC power supply** for the Arduino

#. a **"Main" track,** aka "Operations" track - most people already have this: it's your layout!
#. a **"Programming" track,** aka "Service" track - an isolated short section of track that you will use to program locomotives
#. a **Train** - Specifically, a locomotive equipped with a DCC decoder (either a standard or sound decoder)

.. [#inst]  The Instructions on the following pages assume that that you will use a WiFi Shield.
.. [#jmri]  Requires |JMRI| installed on a computer.

Next Steps - Purchasing Parts
=============================

Click :doc:`here <purchasing>` or click the "next" button to see what you need to purchase to create your |EX-CS|.

.. toctree::
    :hidden:

    purchasing
    assembly
    wifi-setup
    installer
    testing
    controllers
    diagnosing-issues
