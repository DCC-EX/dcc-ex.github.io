.. include:: /include/include.rst
.. include:: /include/include-l3.rst
|EX-CS-LOGO|

|conductor| |tinkerer| |engineer|

*********************
DCC accessory signals
*********************

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

Important considerations for DCC accessory signals
==================================================

Before connecting DCC accessory signals, you will need to read the manufacturer's information on how they should be connected, and to understand the default DCC address in use, and how to change the address if necessary.

You will also need to be aware that should a short circuit occur on the track, resulting in the |EX-CS| turning the track power off, any DCC accessories obtaining power and DCC commands from the track will not be able to be operated.

Defining DCC accessory signals as light signal objects
======================================================

|NOT-IN-PROD-VERSION|

If you are running the latest unreleased development version of the |EX-CS| software, it is possible to use |EX-R|'s signal event handler commands to operate DCC accessory signals just like a light signal.

There are three event handlers available:

- ``ONRED(signal_vpin)`` - triggers an activity to occur when sending a "RED" aspect to a signal
- ``ONAMBER(signal_vpin)`` - triggers an activity to occur when sending an "AMBER" aspect to a signal
- ``ONGREEN(signal_vpin)`` - triggers an activity to occur when sending a "GREEN" aspect to a signal

In order to utilise these commands, you will need to define a light signal object using a valid but available Vpins, and then define macros for each of the signal event handlers.

These definitions and macros are added to your "myAutomation.h" file.

Let's take an example using a DCC accessory signal that uses linear DCC address 101 for red, 102 for amber, and 103 for green:

.. code-block:: cpp

  SIGNAL(5000, 5001, 5002)
  
  ONRED(5000)
    ACTIVATEL(101)
  DONE
  
  ONAMBER(5000)
    ACTIVATEL(102)
  DONE

  ONGREEN(5000)
    ACTIVATEL(103)
  DONE

In this example, we define a light signal with three valid Vpins that are not in use anywhere; 5000, 5001, and 5002. This defines a signal object that can be associated with signal event handlers.

Next, we define what happens when a red aspect command is sent to the signal, which is to activate the DCC linear address 101.

We create the same event handler for the amber and green aspects, noting that each event handler only refers to the Vpin assigned to the red aspect.

Once defined, any aspect command sent to this signal will control the DCC accessory signal correctly.

Connecting the signals
======================

While DCC accessories are typically connected to a track in order to successfully receive DCC commands, you will need to refer to the manufacturer's documentation on how this is accomplished for the particular brand and model of DCC accessory signals you are using.

Controlling DCC signals
=======================

If you have defined your DCC accessory signals as light signals, then controlling these is exactly the same as light or semaphore signals, skip to :doc:`/ex-commandstation/accessories/signals/signal-control` for information on controlling signals.

If, instead your signals will be controlled as per any other DCC accessory device, you will need to familiarise yourself with the :ref:`ex-rail/ex-rail-reference:dcc accessory decoder commands` as outlined in the |EX-R| reference.