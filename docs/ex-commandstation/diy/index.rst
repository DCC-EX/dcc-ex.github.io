.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-cs.rst
|EX-CS-LOGO|

***********************
DIY - Getting Started
***********************

|conductor| |tinkerer| |engineer| |support-button|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

In order to get the most out of this website, we only ask you at first to make 2 choices, the first was to self-identify your "level" with regards to DCC-EX. If you have not chosen whether you are a Conductor, Tinkerer, or Engineer, please go to XXX before proceeding further.

Your next choice will be whether you want to choose the "Ready-To-Run" path or the "Do-It-Yourself" path. We will get to that in a menus, but first let's define what a Command Station is.

What is EX-CommandStation?
==========================

EX-CommandStation is 2 things. It is the name of the software that runs on different hardware platforms, and it is the actual hardware with our software installed that runs you train layout. That means that when you apply power to your Command Station (CS) it will be an |EX-CS| running the latest version of the |EX-CS| software.

An |EX-CS| is a simple, but powerful, DCC Command Station which you can purchase ready-to-run or assemble yourself from widely available Arduino boards. It supports much of the NMRA Digital Command Control (DCC) standards, including:

* Simultaneous control of multiple locomotives
* Control of all cab functions (F0-F28 and F29-F68)
* Control of accessory/function decoders (F0-F28 and F29-F68)
* Main Track: Write configuration variable (CV) bytes and set/clear specific CV bits (aka Programming on Main, or POM)
* Programming Track: Same as the main track with the addition of reading CV bytes

It includes advanced features such as:

* A |WiThrottle server| implementation, 
* General purpose inputs and outputs (I/O) for extensibility, and 
* |JMRI| integration

Ready-To-Run or DIY?
=====================



The following pages will instruct you on how to build an |EX-CS| including assembling your hardware, installing software, and running your first train. After that, we will provide examples for how the base system can be extended and upgraded.

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

2. a **Throttle (Controller)** - Something to control your trains with.  |BR| Such as our |EX-WT|, or other apps like |JMRI|, |Engine Driver|, |WiThrottle|, etc.
3. Power - The Arduino and the Motor shields need to be powered separately, so 
 
  - a **9-14v DC power supply** for the motor shield to the track, and 
  - a **5-9v DC power supply** for the Arduino

4. a **"Main" track,** aka "Operations" track - most people already have this: it's your layout!
5. a **"Programming" track,** aka "Service" track - an isolated short section of track that you will use to program locomotives
6. a **Train** - Specifically, a locomotive equipped with a DCC decoder (either a standard or sound decoder). Ideally, it should be a loco already proven to work on DCC. Otherwise, if you have a problem, you may not be able to tell if the problem is the decoder or the EX-CommandStation

Next Steps - Purchasing Parts
=============================

Click :doc:`here <purchasing>` or click the "next" button to see what you need to acquire to create your |EX-CS|.

----

.. [#inst]  The Instructions on the following pages assume that that you will use a WiFi Shield.
.. [#jmri]  Requires |JMRI| installed on a computer.

.. toctree::
    :hidden:

    purchasing
    assembly
    wifi-setup
    ../installer.rst
    ../controllers.rst
    ../testing.rst
    /support/ex-cs-troubleshooting
    /support/wifi-at-version