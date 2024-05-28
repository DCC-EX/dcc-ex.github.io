.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-description.rst
|EX-CS-LOGO|

*********************
DCC accessory signals
*********************

|conductor| |tinkerer| |engineer| |support-button|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

Important considerations for DCC accessory signals
==================================================

Before connecting DCC accessory signals, you will need to read the manufacturer's information on how they should be connected, to understand the default DCC addresses in use, and how to change them.

You will also need to be aware that should a short circuit occur on the track, resulting in the |EX-CS| turning the track power off, any DCC accessories obtaining power and DCC commands from the track will not be able to be operated.

Defining DCC accessory signals
==============================

As DCC accessory signals are operated the same as any other DCC accessory device, there is no need to define specific objects to operate DCC accessory signals, and instead you can use the DCC accessory commands provided in |EX-R|:

- ``ACTIVATE(addr, sub_addr)``
- ``DEACTIVATE(addr, sub_addr)``
- ``ACTIVATEL(addr)``
- ``DEACTIVATEL(addr)``

Once again, you will need to refer to the manufacturer's documentation on how the signals operate in order to know which commands will be required to operate the signals.

Connecting the signals
======================

While DCC accessories are typically connected to a track in order to successfully receive DCC commands, you will need to refer to the manufacturer's documentation on how this is accomplished for the particular brand and model of DCC accessory signals you are using.

Controlling your DCC signals
============================

Continue on to the next page for details on signal control.